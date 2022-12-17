from .send_email import mail_sending
from server.celery import app

@app.task
def mail_sending_task(recipient, password):
    mail_sending(recipient, password)