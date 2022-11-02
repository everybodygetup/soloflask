from flask import Blueprint,request,render_template,redirect,url_for,flash
from app.extensions import db
from app.posts.models import TnVed

posts = Blueprint('posts', __name__, template_folder='templates')

@posts.route('/posts/<int:id>/update',methods=['POST','GET'])
def post_update(id):
    """Редактировать запись"""
    ved_db = TnVed.query.get(id)
    if request.method == "POST":
        ved_db.title = request.form['title']
        ved_db.intro = request.form['intro']
        ved_db.text = request.form['text']

        try:
            db.session.commit()
            return redirect('/posts')
        except:
            return "Произошла ошибка"
    else:
        
        return render_template('posts/post_update.j2', ved_db=ved_db)


    
@posts.route('/posts/<int:id_post>/del')
def post_delete(id_post):
    """Удаление из БД"""
    ved_db = TnVed.query.get_or_404(id_post)
    ved_db.delete()
    flash('Код удален')
    return redirect('/posts')
    

@posts.route('/posts')
def post():
    """Показывает посты из БД ved/ved2"""
    ved_db = TnVed.query.order_by(TnVed.date.desc()).all()
    return render_template('posts/posts.j2',ved_db=ved_db)


@posts.route('/posts/<int:id>')
def post_detail(id):
    """Обработка нужного url адреса"""
    ved_db = TnVed.query.get(id)
    return render_template('posts/post_detail.j2',ved_db=ved_db)

