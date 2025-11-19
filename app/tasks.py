from celery import Celery
from datetime import datetime
import smtplib
import os
 
# Load environment variables
from dotenv import load_dotenv
load_dotenv()
 
CELERY_BROKER_URL = 'pyamqp://guest@localhost//'
CELERY_RESULT_BACKEND = 'rpc://'
 
celery = Celery('tasks', broker=CELERY_BROKER_URL, backend=CELERY_RESULT_BACKEND)
 
# Celery task to send email
@celery.task
def send_email_task(recipient):
    sender_email = os.getenv("SMTP_EMAIL")
    sender_password = os.getenv("SMTP_PASSWORD")
    subject = "Test Email from Messaging System"
    body = "This is a test email sent asynchronously using Celery!"
    message = f"Subject: {subject}\n\n{body}"
   
    try:
        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
            server.login(sender_email, sender_password)
            server.sendmail(sender_email, recipient, message)
        return f"Email sent to {recipient}"
    except Exception as e:
        return str(e)
 
# Celery or synchronous task to log time
def log_time_task():
    with open("logs/app.log", "a") as f:
        f.write(f"Logged time: {datetime.now()}\n")