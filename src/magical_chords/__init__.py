import click
from flask import render_template
import flask
from flask import request
from magical_chords import chord_formatter


app = flask.Flask(__name__, static_url_path='/web/')
app.config["DEBUG"] = True


# database creation
@click.command('init-db')
def init_db():
    print('hello_world!')

app.cli.add_command(init_db)


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
    return render_template('library_layout.html')



if __name__ == "__main__":
    app.run()

