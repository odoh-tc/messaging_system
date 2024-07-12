from celery import Celery
import smtplib
from email.mime.text import MIMEText
import os

celery_app = Celery('tasks')
celery_app.config_from_object('celeryconfig')

@celery_app.task
def send_email(email: str):
    msg = MIMEText("This is a test email.")
    msg["Subject"] = "Test Email"
    msg["From"] = os.getenv("EMAIL_FROM")
    msg["To"] = email

    try:
        with smtplib.SMTP(os.getenv("SMTP_SERVER"), os.getenv("SMTP_PORT")) as server:
            server.starttls()
            server.login(os.getenv("SMTP_USER"), os.getenv("SMTP_PASSWORD"))
            server.sendmail(os.getenv("EMAIL_FROM"), [email], msg.as_string())
        return f"Email sent to {email}"
    except Exception as e:
        return f"Failed to send email to {email}: {str(e)}"
