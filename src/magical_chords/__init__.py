import click
import flask
from flask import render_template, request
from magical_chords import chord_formatter
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import or_
from magical_chords.configs import config
from magical_chords.importer import song_importer


app = flask.Flask(__name__, static_url_path='/web/')
config.configure_app(app)


db = SQLAlchemy(app)


class Chords(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    author = db.Column(db.String(100), nullable=False)
    title = db.Column(db.String(300), nullable=False)
    song_content = db.Column(db.Text, nullable=False)
    song_preview = db.Column(db.Text, nullable=False)


# database creation
@click.command('init-db')
def init_db():
    db.create_all()

    num_songs = Chords.query.count()
    if num_songs == 0:          
        for author, title, song_content in song_importer.chopro_gen:
            song = Chords(author=author.replace('.', ' '), title=title, song_content=song_content, song_preview=chord_formatter.song_preview(song_content))
            db.session.add(song)
            db.session.commit()



app.cli.add_command(init_db)
# this regiters the function so shell can recognize it


# chord formatter
@app.route('/format_chordpro/', methods=['POST'])
def format_chordpro():
    chord = request.data.decode()
    return chord_formatter.format(chord)


# templates rendering
# home page
@app.route('/')
def root_home(name=None):
    return render_template('home_layout.html')

# library & search
@app.route('/library/', methods=['GET'])
def root_library():
    songs = Chords.query.order_by(
        Chords.author.asc(), Chords.title.asc()).all()
    return render_template('library_layout.html', songs=songs)


@app.route('/search/', methods=['GET'])
def root_search():
    search_text = request.args.get('search_text')
    songs = Chords.query.filter(
        or_(
            Chords.author.ilike(f"%{search_text}%"),
            Chords.title.ilike(f"%{search_text}%"),
            Chords.song_content.ilike(f"%{search_text}%")
        )
    ).order_by(Chords.author.asc(), Chords.title.asc())
    results_message = f"Your search '{search_text}' returned {songs.count()} result(s)."
    return render_template('library_layout.html', songs=songs, results_message=results_message, search_text=search_text)


@app.route('/song/', methods=['GET'])
def root_song():
    song_id = request.args.get('song_id')
    song = Chords.query.filter_by(id=song_id).first()
    formatted_song = Chords(author=song.author, title=song.title,
                            song_content=chord_formatter.format(song.song_content))
    return render_template('song_layout.html', song=formatted_song)

# artists page
@app.route('/artists/', methods=['GET'])
def root_artists():
    songs = Chords.query.order_by(
        Chords.author.asc(), Chords.title.asc()).distinct(Chords.author)
    return render_template('artists_layout.html', songs=songs)


@app.route('/artists_songs/', methods=['GET'])
def root_artists_songs():
    artist = request.args.get('artist')
    songs = Chords.query.filter_by(author=artist).all()
    return render_template('library_layout.html', songs=songs)

# insert & about pages
@app.route('/insert/')
def root_insert(name=None):
    return render_template('insert_layout.html')

@app.route('/about/')
def root_about(name=None):
    return render_template('about_layout.html')


if __name__ == "__main__":
    app.run()
