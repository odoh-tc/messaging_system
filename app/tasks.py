from celery import Celery
import smtplib
from email.mime.text import MIMEText
import os
import logging

# Setup Celery
celery_app = Celery('tasks')
celery_app.config_from_object('celeryconfig')

@celery_app.task(bind=True, max_retries=3)
def send_email(self, email: str):
    msg = MIMEText("This is a test email.")
    msg["Subject"] = "Test Email"
    msg["From"] = os.getenv("EMAIL_FROM")
    msg["To"] = email

    try:
        with smtplib.SMTP_SSL(os.getenv("SMTP_SERVER"), os.getenv("SMTP_PORT")) as server:
            server.login(os.getenv("SMTP_USER"), os.getenv("SMTP_PASSWORD"))
            server.sendmail(os.getenv("EMAIL_FROM"), [email], msg.as_string())
        logging.info(f"Email sent to {email}")
    except Exception as e:
        logging.error(f"Failed to send email to {email}: {str(e)}")
        self.retry(exc=e)
