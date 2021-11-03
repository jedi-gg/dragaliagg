#!/bin/bash
python manage.py collectstatic --noinput  # Collect static files
python manage.py compress

exec gunicorn core.wsgi:application \
    --config /srv/app/_docker/django/gunicorn.py