Messaging System with RabbitMQ, Celery, Nginx, and Python
Project Overview
This project implements a simple messaging system that demonstrates asynchronous task processing using RabbitMQ as a message broker and Celery as a task queue. It is served via a Python web application behind Nginx, exposing endpoints to:
   •	Send an email asynchronously via SMTP.
   •	Log the current server time.
External testing is possible using ngrok.
System Architecture
[ Client ] --> [ Nginx Reverse Proxy ] --> [ Python App (Flask/FastAPI) ]
                                        |---> [ Celery Worker ] --> [ RabbitMQ ]
                                        |---> Logging (synchronous)
   •	Nginx: Reverse proxy forwarding HTTP requests to Python app.
   •	Python Application: Provides two endpoints:
      o	?sendmail=<recipient_email>  → Sends an email asynchronously via Celery.
      o	?talktome  → Logs current server time to app.log.
   •	Celery + RabbitMQ: Handles asynchronous email sending.
   •	Ngrok: Exposes local server to a public URL for testing.


Features:
1. Email Sending (?sendmail=<email>)
   •	Accepts an email address as a query parameter.
   •	Publishes a "send email" task to RabbitMQ.
   •	Celery worker sends email asynchronously using SMTP.
2. Logging Time (?talktome)
   •	Logs the current server timestamp to app.log.
   •	Demonstrates synchronous logging functionality.
3. Task Execution
   •	Email tasks: Asynchronous.
   •	Logging tasks: Synchronous (can be converted to asynchronous via Celery if needed).
________________________________________
Technologies Used
   •	RabbitMQ – Message broker.
   •	Celery – Task queue manager.
   •	Flask / FastAPI – Python web framework.
   •	Gunicorn / Uvicorn – Application server.
   •	Nginx – Reverse proxy.
   •	SMTP – Email sending.
   •	Ngrok – Public exposure.
   •	Python 3.9+
Installation & Setup
1. Install Dependencies
# Python packages
pip install flask celery[redis] gunicorn uvicorn python-dotenv

# System dependencies
sudo apt install rabbitmq-server nginx
2. Start RabbitMQ
sudo service rabbitmq-server start
3. Configure Celery
   •	Define Celery tasks for email sending and logging.
# tasks.py
from celery import Celery

celery = Celery('tasks', broker='pyamqp://guest@localhost//')
4. Develop Python Application
   •	Flask/FastAPI routes:
       /action?sendmail=<email>
       /action?talktome
   •	Tasks are called when endpoints are hit.
5. Configure SMTP
   •	Use environment variables for credentials.
   •	Celery worker sends test email using SMTP.
6. Deploy Behind Nginx
   •	Configure reverse proxy from Nginx → Gunicorn/ Uvicorn.
7. Expose Public Endpoint
ngrok http 80
________________________________________
Testing
Email Endpoint
https://<ngrok-id>.ngrok.io/action?sendmail=test@example.com
   •	Expected: Email sent asynchronously.
Logging Endpoint
https://<ngrok-id>.ngrok.io/action?talktome
   •	Expected: Current timestamp appended to app.log.
Conclusion
This project demonstrates asynchronous task processing in Python using RabbitMQ and Celery. With Nginx and ngrok, it simulates production-ready patterns like task queuing, reverse proxying, and background job execution.
