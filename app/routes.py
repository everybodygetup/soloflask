from flask import flash, g, redirect, render_template, request, url_for

from app import app,db
from app.forms import LoginForm
from app.models import TnVed


@app.before_first_request
def create_tables():
    db.create_all()



@app.route('/')
@app.route('/index')
def index():
    return render_template('index.j2')


@app.route('/about')
def about():
    return render_template('about.j2')



@app.route('/ved',methods=['POST','GET'])
def ved():
    if request.method == "POST":
        title = request.form['title']
        intro = request.form['intro']
        text = request.form['text']

        ved_db = TnVed(title=title,intro=intro,text=text)

        try:
            db.session.add(ved_db)
            db.session.commit()
            return redirect('/')
        except:
            return "Произошла ошибка"
    return render_template('ved.j2')


@app.route('/user/<string:name>/<int:id>')
def user(name,id):
    return 'User page: ' + name + '-' + str(id)

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login requested for user {}, remember_me={}'.format(
            form.username.data, form.remember_me.data))
        return redirect(url_for('index'))
    return render_template('login.j2', title='Sign In', form=form)

