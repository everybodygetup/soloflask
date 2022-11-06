from flask import Blueprint,request,render_template,redirect,url_for,flash
from app.extensions import db
from app.parts.models import SpareParts

parts = Blueprint('parts', __name__, template_folder='templates')

@parts.route('/parts/<int:id>/update',methods=['POST','GET'])
def parts_update(id):
    """Редактировать запись"""
    ved_db = SpareParts.query.get(id)
    if request.method == "POST":
        ved_db.title = request.form['title']
        ved_db.intro = request.form['intro']
        ved_db.text = request.form['text']

        try:
            db.session.commit()
            return redirect('/parts')
        except:
            return "Произошла ошибка"
    else:
        
        return render_template('parts/parts_update.j2', ved_db=ved_db)


    
@parts.route('/parts/<int:id_post>/del')
def parts_delete(id_post):
    """Удаление из БД"""
    ved_db = SpareParts.query.get_or_404(id_post)
    ved_db.delete()
    flash('Код удален')
    return redirect('/parts')
    

@parts.route('/parts')
def part():
    """Показывает посты из БД ved/ved2"""
    ved_db = SpareParts.query.order_by(SpareParts.date.desc()).all()
    return render_template('parts/parts.j2',ved_db=ved_db)


@parts.route('/parts/<int:id>')
def parts_detail(id):
    """Обработка нужного url адреса"""
    ved_db = SpareParts.query.get(id)
    return render_template('parts/parts_detail.j2',ved_db=ved_db)

