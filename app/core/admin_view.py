from flask import Blueprint, redirect, render_template, url_for
from flask_security import login_required, permissions_required, roles_required

from app.core.models import Role, User, user_datastore
from app.extensions import db


admin = Blueprint("admin", __name__, template_folder="templates")



@admin.get("")
#@login_required
#@permissions_required("admin-read")
def index():
    """Главная страница админки."""
    return render_template("admin/index.j2")