#!/bin/bash
source venv/bin/activate
celery -A app.tasks.celery worker --loglevel=info