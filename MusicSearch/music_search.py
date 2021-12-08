from flask import Flask, render_template, flash, redirect
from flask_bootstrap import Bootstrap
from flask_fontawesome import FontAwesome
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
from datetime import datetime
from random import shuffle, randint
import random
from PIL import Image


app = Flask(__name__)
bootstrap = Bootstrap(app)


@app.route('/', methods=('GET', 'POST'))
def home():
    # form = SearchForm()
    # if not form.validate_on_submit():
    #     return redirect('/')
    return render_template('home.html')


@app.route('/random', methods=('GET', 'POST'))
def random():
    # form = SearchForm()
    # if not form.validate_on_submit():
    #     return redirect('/')
    return render_template('random.html')


@app.route('/album', methods=('GET', 'POST'))
def album():
    # form = SearchForm()
    # if not form.validate_on_submit():
    #     return redirect('/')
    return render_template('album.html')


@app.route('/contact', methods=('GET', 'POST'))
def contact():
    # form = SearchForm()
    # if not form.validate_on_submit():
    #     return redirect('/')
    return render_template('contact.html')
