# Course: CST205
# Title: Music Search
# Abstract: A user will be able to search for their favorite artisits album, and get random suggestions
# Authors: Hernan Hernandez, Ethan Garnica, Brielle Lacey, Jack Lopez
# Date: December 15, 2021
# Hernan - Worked on HTML design and search function as well as album output
# Ethan - Worked on creating and adding to Database as well as the output of a random album
# Brielle - Worked on contact page

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

# creates search form


class Search(FlaskForm):
    artist = StringField(
        'Artist', validators=[DataRequired()]
    )
    submit = SubmitField('Submit')

# Gets all artists names and stores in list


def get_artist(song_info):
    artistList = []
    for i in song_info:
        artist = i.get('artist').lower()
        artistList.append(artist)
    return sorted(artistList)


# Home search function
@app.route('/', methods=('GET', 'POST'))
def home():
    form = Search()
    # gets artist
    artists = get_artist(song_info)
    message = ""
    # if form is valid do function
    if form.validate_on_submit():
        userInput = form.artist.data
        if userInput.lower() in artists:
            # empty the form field
            form.artist.data = ""
            artist_id = userInput
            # redirect the browser to another route and template
            return redirect(url_for('album', artist_id=artist_id))
        else:
            # outputs on console
            message = "That search is not in our database."
    return render_template('home.html', artists=artists, form=form,  message=message)


@app.route('/random', methods=('GET', 'POST'))
def random():
    song_stuff = song_info[randint(0, 34)]

    # form = SearchForm()
    # if not form.validate_on_submit():
    #     return redirect('/')
    return render_template('random.html', info=song_stuff)

# album page for artist


@app.route('/album/<artist_id>', methods=('GET', 'POST'))
def album(artist_id):
    name = ''
    # Iterate through our database
    # if artist input matches artist in database send info to page
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
