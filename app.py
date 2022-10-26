from flask import Flask,url_for, request, render_template


app = Flask(__name__)





@app.route('/')
def index():
    return render_template('index.j2')



@app.route('/about')
def about():
    return render_template('about.j2')


