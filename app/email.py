from datetime import datetime

from app.extensions import executor
from flask import current_app, render_template
from flask_mailman import EmailMessage as Message
from flask_security import MailUtil


def sendmail_callback(future):
    """

    :param future:

    """
    print(
        f"{datetime.now()} => Почта {'успешно' if future.done() else 'не'} отправлена"
    )


class SecMailUtil(MailUtil):
    """Кастомный класс для отправки почты для flask-security."""

    def send_mail(
        self, template, subject, recipient, sender, body, html, user, **kwargs
    ):
        """Send an email via the Flask-Mailing extension.

        :param template:
        :param subject:
        :param recipient:
        :param sender:
        :param body:
        :param html:
        :param user:
        :param **kwargs:
        """
        sender = f"Робот с сайта «{current_app.config['APP_NAME']}» <{current_app.config['MAIL_USERNAME']}>"
        recipients = [recipient]
        current_app.logger.debug(body)
        current_app.logger.info(
            f"Отправляем письмо для {recipient} пользователем {user}"
        )
        executor.add_default_done_callback(sendmail_callback)
        executor.submit(send_async_email, subject, recipients, sender, body, html)


def send_email(subject=None, **kwargs):
    """

    :param subject: Default value = None)
    :param **kwargs:

    """
    sender = f"Робот с сайта «{current_app.config['APP_NAME']}» <{current_app.config['MAIL_USERNAME']}>"
    time = datetime.now().ctime()
    recipients = current_app.config["MAIL_ADMINS"]
    body = None
    html = render_template("email/message.j2", subject=subject, time=time, **kwargs)
    current_app.logger.info("Отправляем письмо админам")
    executor.add_default_done_callback(sendmail_callback)
    executor.submit(send_async_email, subject, recipients, sender, body, html)


def send_async_email(subject, recipients, sender, body=None, html=None):
    """

    :param subject:
    :param recipients:
    :param sender:
    :param body:  (Default value = None)
    :param html: (Default value = None)

    """
    msg = Message(subject=subject, from_email=sender, to=recipients)
    if body:
        msg.body = body
    else:
        msg.body = html
        msg.content_subtype = "html"
    msg.send()
