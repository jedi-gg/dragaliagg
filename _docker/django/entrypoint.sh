#!/bin/bash
python manage.py collectstatic --noinput  # Collect static files
python manage.py migrate
python manage.py cache-clear

exec gunicorn core.wsgi:application \
    --config /srv/app/_docker/django/gunicorn.py