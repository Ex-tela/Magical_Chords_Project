from sqlalchemy import or_
import click
from flask import render_template
import flask
from flask import request
from magical_chords import chord_formatter
from flask_sqlalchemy import SQLAlchemy



app = flask.Flask(__name__, static_url_path='/web/')
app.config["DEBUG"] = True
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:123@localhost/magical_chords'

db = SQLAlchemy(app)

class Chords(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    author = db.Column(db.String(100), nullable=False)
    title = db.Column(db.String(300), nullable=False)
    song_content = db.Column(db.Text, nullable=False)


# database creation
@click.command('init-db')
def init_db():
    db.create_all()

    num_songs = Chords.query.count()
    if num_songs == 0:
        song1 = Chords(author='The Beatles', title="We Can Work It Out", song_content="We Can[D] Work It [G]Out")
        song2 = Chords(author='Jefferson Airplane', title="Somebody to Love", song_content="Don't you[D] need [G]somebody to lo[C]ve?")
    
        db.session.add(song1)
        db.session.add(song2)
        db.session.commit()


app.cli.add_command(init_db)
# this regiters the function so shell can recognize it


# chord formatter "import"
@app.route('/format_chordpro/', methods=['POST'])
def format_chordpro():
   chord = request.data.decode()
   return chord_formatter.format(chord)


# templates rendering
@app.route('/')
def root_home(name=None):
    return render_template('home_layout.html')

@app.route('/about/')
def root_about(name=None):
    return render_template('about_layout.html')

@app.route('/library/', methods=['GET'])
def root_library():
    songs = Chords.query.order_by(Chords.author.asc(), Chords.title.asc()).all()
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
    formatted_song = Chords(author=song.author, title=song.title, song_content=chord_formatter.format(song.song_content))
    return render_template('song_layout.html', song=formatted_song)


if __name__ == "__main__":
    app.run()