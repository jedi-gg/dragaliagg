FROM python:3.8

ENV TERM=xterm-256color \
    PYTHONUNBUFFERED=1 \
    DJANGO_SETTINGS_MODULE="core.settings"

RUN apt-get update && apt-get install -y nano default-mysql-client iputils-ping

RUN echo 'alias l="ls -al"' >> ~/.bashrc
RUN echo 'alias pm="python manage.py"' >> ~/.bashrc
RUN echo 'alias pmr="python manage.py runserver 0.0.0.0:8000"' >> ~/.bashrc

WORKDIR "/srv/app"

ADD requirements.txt /tmp
RUN pip install -r /tmp/requirements.txt

# Create Log Files
RUN mkdir -p /var/log/applogs/

# Add Entrypoint file
COPY _docker/django/entrypoint.sh /
RUN chmod +x /entrypoint.sh

CMD ["/bin/bash"]