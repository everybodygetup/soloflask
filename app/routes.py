from flask import flash, g, redirect, render_template, request, url_for

from app import app

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.j2')


@app.route('/about')
def about():
    return render_template('about.j2')


