from flask import Flask, render_template, flash, redirect
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

if __name__ == "__main__":
    app.run(host='127.0.0.9', port=4455, debug=True)

bootstrap = Bootstrap(app)


@app.route('/', methods=('GET', 'POST'))
def home():
    name = ' '
    artistList = []
    for i in song_info:
        artist = i.get('artist')
        artistList.append(artist)
    if name in artistList:
        return

    return render_template('home.html', artistList=artistList)


@app.route('/random', methods=('GET', 'POST'))
def random():
    # form = SearchForm()
    # if not form.validate_on_submit():
    #     return redirect('/')
    return render_template('random.html', info=song_info)


# print(song_info[1])
# for i in song_info:
#     print(i.get('artist'))
# artistList = []
# for i in song_info:
#     artist = i.get('artist')
#     artistList.append(artist)
# print(artistList)


@app.route('/album/<artist_id>', methods=('GET', 'POST'))
def album(artist_id):
    # print(artistList)
    artist = ''
    artistList = []
    for i in song_info:
        if(artist_id == i.get('artist')):
            artist = i.get('artist')
            print(artist_id)
    artist_id = artist
    print(artist_id)
    # artist = i.get('artist')
    # print(artist_id)
    # EartistList.append(artist)

    # artist_id = artistList
    # if albumName == song_info[1]
    # form = SearchForm()
    # if not form.validate_on_submit():
    #     return redirect('/')
    return render_template('album.html', artist_id=artist_id, info=song_info)


@ app.route('/contact', methods=('GET', 'POST'))
def contact():
    # form = SearchForm()
    # if not form.validate_on_submit():
    #     return redirect('/')
    return render_template('contact.html')
