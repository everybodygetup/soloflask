from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, TextAreaField, TelField, EmailField
from wtforms.validators import DataRequired, Email


class KodForm(FlaskForm):
    find = StringField('слово или код', validators=[DataRequired(message='Обязательное поле')])
    findButton = SubmitField('найти')


class FeedbackForm(FlaskForm):
    """Форма отзыва."""

    first_name = StringField("Имя")
    last_name = StringField("Фамилия")
    phone = TelField("Номер телефона")
    email = EmailField(
        "Email",
        validators=[
            DataRequired("Email обязателен для заполнения"),
            Email("Email введён неправильно"),
        ],
    )
    text = TextAreaField("Сообщение", validators=[DataRequired("Сообщение обязательно для заполнения")])
    submit = SubmitField("Отправить")