from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField,TextAreaField
from wtforms.validators import DataRequired

class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Sign In')


class VedForm(FlaskForm):
    """Форма заполнения ТНВЭД."""

    title = StringField("Заголовок")
    text = TextAreaField("Код")
    submit = SubmitField("Добавить код")