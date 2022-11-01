from flask import flash, g, redirect, render_template, request, url_for

from app import app,db
from app.forms import LoginForm,VedForm
from app.models import TnVed
from flask_security import current_user












#@app.route('/login', methods=['GET', 'POST'])
#def login():
#    form = LoginForm()
#    if form.validate_on_submit():
#        flash('Login requested for user {}, remember_me={}'.format(
#            form.username.data, form.remember_me.data))
#       return redirect(url_for('index'))
#    return render_template('login.j2', title='Sign In', form=form)



#@app.route("/ved2", methods=["GET", "POST"])
#@roles_accepted("admin")
#def ved2():
# """Создание бд кодов."""
#    ved_form = VedForm(obj=request.form)
#
#   if ved_form.validate_on_submit():
#        vd_db = TnVed(
#            title=request.form.get("title"),
#            text=request.form.get("text")
#        )
#        db.session.add(vd_db)
#        db.session.commit()
#        flash("Код ТНВЭД добавлен", "success")
#        return redirect(url_for("posts", id_feedback=vd_db.id))
#    return render_template("ved2.j2", form=ved_form)






