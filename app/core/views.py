from flask import Blueprint, request, render_template, redirect, flash, g
from flask_security import current_user, login_required
from app.extensions import db
from app.parts.models import SpareParts
from app.core.models import UserSubmit, user_datastore
from app.core.forms import KodForm, FeedbackForm


core = Blueprint('core', __name__, template_folder='templates')


@core.before_app_request
def create_tables():
    db.create_all()
    user_datastore.find_or_create_role(
        name="admin",
        permissions={
            "admin-read",
            "admin-write",
            "user-read",
            "user-write",
            "partner-read",
            "partner-write",
        },
    )
    user_datastore.find_or_create_role(
        name="monitor", permissions={"admin-read", "user-read"}
    )
    user_datastore.find_or_create_role(
        name="partner", permissions={"partner-read", "partner-write"}
    )
    user_datastore.find_or_create_role(
        name="user", permissions={"user-read", "user-write"}
    )
    user_datastore.find_or_create_role(name="reader", permissions={"user-read"})
    db.session.commit()
    

@core.route('/index', methods=['GET', 'POST'])
@core.route('/', methods=['GET', 'POST'])
def index():
    form = KodForm()
    if form.validate_on_submit():
        kod_search = SpareParts.query.filter(SpareParts.title.like(f'%{form.find.data}%')).all()
        return render_template('index.j2', kod_search=kod_search, form=form)
    return render_template('index.j2', form=form)


@core.route('/about', methods=['GET', 'POST'])
#@login_required
def about():
    """Главная страница сайта."""
    feedback_form = FeedbackForm(obj=request.form)

    if feedback_form.validate_on_submit():
        core_db = UserSubmit(
            fist_name=request.form.get("first_name"),
            last_name=request.form.get("last_name"),
            email=request.form.get("email"),
            text=request.form.get("text"),
            user_id=current_user.id,
        )
        core_db.save()
        return render_template('index.j2', form=feedback_form)
    return render_template('about.j2', form=feedback_form)


@core.route('/lk')
def lk():
    g.page_title = 'Личный кабинет'
    return render_template('lk/index.j2')
