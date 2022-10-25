from flask import Flask,url_for, request, render_template

app = Flask(__name__)

app.run(debug=True)

@app.route('/')
def index():
    return 'Privet Artem'



@app.route('/hello/')
@app.route('/hello/<name>')
def hello(name=None):
    return render_template('hello.j2', name=name)


@app.route('/about')
def about():
    return 'about page'


