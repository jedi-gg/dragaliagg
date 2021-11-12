#!/bin/bash
python manage.py collectstatic --noinput  # Collect static files
python manage.py migrate

exec gunicorn core.wsgi:application \
    --config /srv/app/_docker/django/gunicorn.py