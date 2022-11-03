from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField,TextAreaField
from wtforms.validators import DataRequired


class KodForm(FlaskForm):
    find = StringField('слово или код', validators=[DataRequired(message='Обязательное поле')])
    findButton = SubmitField('найти')