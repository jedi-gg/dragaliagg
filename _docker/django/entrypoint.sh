#!/bin/bash
pip-sync
python manage.py migrate

if [ "$ENV" == "PROD" ]; then
    python manage.py collectstatic --noinput  # Collect static files
    python manage.py cache-clear
    exec gunicorn core.wsgi:application \
        --config /srv/app/_docker/django/gunicorn.py
fi

if [ "$ENV" == "DEV" ]; then
    exec python manage.py runserver 0.0.0.0:8000
fi