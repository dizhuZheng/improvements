from threading import Thread
from flask import current_app
from flask_mail import Message
from .extensions import mail
import os

def _send_async_mail(app, message):
    with app.app_context():
        mail.send(message)


def send_mail(subject, to, html):
    app = current_app._get_current_object()
    message = Message(subject, recipients=[to], html=html)
    thr = Thread(target=_send_async_mail, args=[app, message])
    thr.start()
    mail.send(msg)
    return thr

# msg_title = 'Hello There.'
# msg_sender = os.environ.get('MAIL_USERNAME')
# msg_recipients = [email]
# msg_body = 'Hey, I am mail body!'
# msg = Message(msg_title,
#             sender=msg_sender,
#             recipients=msg_recipients)
# msg.body = msg_body