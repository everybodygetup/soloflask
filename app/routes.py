from flask import flash, g, redirect, render_template, request, url_for

from app import app,db
from app.forms import LoginForm,VedForm
from app.models import TnVed
from flask_security import current_user

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
    """Создание бд кодов только из модели напрямую"""
    if request.method == "POST":
        title = request.form['title']
        intro = request.form['intro']
        text = request.form['text']

        ved_db = TnVed(title=title,intro=intro,text=text)

        try:
            db.session.add(ved_db)
            db.session.commit()
            return redirect('/posts')
        except:
            return "Произошла ошибка"
    return render_template('ved.j2')



@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login requested for user {}, remember_me={}'.format(
            form.username.data, form.remember_me.data))
        return redirect(url_for('index'))
    return render_template('login.j2', title='Sign In', form=form)



@app.route("/ved2", methods=["GET", "POST"])
#@roles_accepted("admin")
def ved2():
    """Создание бд кодов."""
    ved_form = VedForm(obj=request.form)

    if ved_form.validate_on_submit():
        vd_db = TnVed(
            title=request.form.get("title"),
            text=request.form.get("text")
        )
        db.session.add(vd_db)
        db.session.commit()
        flash("Код ТНВЭД добавлен", "success")
        return redirect(url_for("posts", id_feedback=vd_db.id))
    return render_template("ved2.j2", form=ved_form)


@app.route('/posts')
def posts():
    """Показывает посты из БД ved/ved2"""
    ved_db = TnVed.query.order_by(TnVed.date.desc()).all()
    return render_template('posts.j2',ved_db=ved_db)


@app.route('/posts/<int:id>')
def post_detail(id):
    """Обработка нужного url адреса"""
    ved_db = TnVed.query.get(id)
    return render_template('post_detail.j2',ved_db=ved_db)