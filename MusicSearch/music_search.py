from flask import Flask, render_template, flash, redirect, request, url_for
from flask_bootstrap import Bootstrap
from flask_fontawesome import FontAwesome
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
from datetime import datetime
from random import shuffle, randint
from flask import request
from song_info import song_info
import random
from PIL import Image


app = Flask(__name__)
app.config['SECRET_KEY'] = 'csumb-otter'
bootstrap = Bootstrap(app)
foo = ['a', 'b', 'c', 'd', 'e']

random_item = random.choice(foo)

print(random_item)


class Search(FlaskForm):
    artist = StringField(
        'Artist', validators=[DataRequired()]
    )
    submit = SubmitField('Submit')


def get_artist(song_info):
    artistList = []
    for i in song_info:
        artist = i.get('artist').lower()
        artistList.append(artist)
    return sorted(artistList)


def get_id(song_info, name):
    for i in song_info:
        print(i)
    return i

# home


@app.route('/', methods=('GET', 'POST'))
def home():
    form = Search()
    if form.is_submitted():
        print("submitted")
    if form.validate():
        print("valid")

    artists = get_artist(song_info)
    message = ""

    if form.validate_on_submit():
        print("yes")
        #flash("successfully sent ")
        userInput = form.artist.data
        print(userInput)
        print(artists)
        if userInput.lower() in artists:
            print(userInput)
            print("IN loop")
            # empty the form field
            form.artist.data = ""
            artist_id = userInput
            print(artist_id)
            # redirect the browser to another route and template
            return redirect(url_for('album', artist_id=artist_id))
        else:
            message = "That search is not in our database."
    return render_template('home.html', artists=artists, form=form,  message=message)


@app.route('/random', methods=('GET', 'POST'))
def random():
    # form = SearchForm()
    # if not form.validate_on_submit():
    #     return redirect('/')
    return render_template('random.html', info=song_info)


@app.route('/album/<artist_id>', methods=('GET', 'POST'))
def album(artist_id):
    name = ''
    for i in song_info:
        if(artist_id == i.get('artist')):
            name = i.get('artist')
            print(name)
            render_template('album.html', artist_id=artist_id, info=song_info)
        else:
            print('error')

    return render_template('album.html', artist_id=artist_id, info=song_info)


@ app.route('/contact', methods=('GET', 'POST'))
def contact():
    # form = SearchForm()
    # if not form.validate_on_submit():
    #     return redirect('/')
    return render_template('contact.html')
