from flask import Blueprint, redirect, render_template, url_for
from flask_security import login_required, permissions_required, roles_required

from app.core.models import Role, User, user_datastore
from app.extensions import db


admin = Blueprint("admin", __name__, template_folder="templates")


@admin.get("/admin")
@login_required
#@permissions_required("admin")
def index():
    """Главная страница админки."""
    return render_template("admin/index.j2")


@admin.get("/users")
@roles_required("admin")
def users():
    """Показ всех пользователей сайта."""
    user_list_db = User.query.all()
    return render_template("admin/users.j2", users=user_list_db)


@admin.get("/user/<int:user_id>/roles")
@roles_required("admin")
def user_roles(user_id):
    """Показываем роли для конкретного пользователя."""
    user_db = User.query.get_or_404(user_id)
    roles_db = Role.query.all()
    return render_template("admin/roles.j2", user=user_db, roles=roles_db)


@admin.get("/user/<int:user_id>/<int:role_id>/add")
@roles_required("admin")
def user_role_add(user_id, role_id):
    """Добавление роли пользователю."""
    user_db = User.query.get_or_404(user_id)
    role_db = Role.query.get_or_404(role_id)
    user_datastore.add_role_to_user(user_db, role_db)
    db.session.commit()
    return redirect(url_for("admin.user_roles", user_id=user_id))