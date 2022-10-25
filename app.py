from flask import Flask,url_for, request, render_template


app = Flask(__name__)





@app.route('/')
def index():
    return render_template('index.j2')


@app.route('/index/')
@app.route('/index/<name>')
def hello(name=None):
    return render_template('index.j2', name=name)


@app.route('/about')
def about():
    return 'about page'


