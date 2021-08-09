#!/bin/sh

set -e

ls -la /vol/
ls -la /vol/web

pip install -r requirements.txt
python manage.py makemigrations --no-input
python manage.py migrate --no-input
python manage.py collectstatic --no-input

gunicorn --workers = 5 --threads = 2 backend.wsgi:application --bind 0.0.0.0:8000

