from flask import Blueprint,request,render_template,redirect,flash
from app.extensions import db
from app.posts.models import TnVed
from app.core.forms import KodForm

core = Blueprint('core', __name__, template_folder='templates')

@core.before_app_request
def create_tables():
    db.create_all()
    

@core.route('/', methods=['GET', 'POST'])
def species():
    form = KodForm()
    if form.validate_on_submit():
        kod_search = KodForm.query.filter(KodForm.name.like(f'%{form.find.data}%')).all()
        return render_template('index.j2', kod_search=kod_search, form=form)
    return render_template('index.j2', form=form)


@core.route('/')
@core.route('/index')
def index():
    '''Главная страница'''
    return render_template('index.j2')



@core.route('/about')
def about():
    return render_template('about.j2')


@core.route('/ved',methods=['POST','GET'])
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
            flash("Код ТНВЭД добавлен", "success")
            return redirect('/posts')
        except:
            return "Произошла ошибка"
    return render_template('ved.j2')