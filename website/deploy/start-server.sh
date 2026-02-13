#!/usr/bin/env bash
# start-server.sh
if [ -n "$DJANGO_SUPERUSER_USERNAME" ] && [ -n "$DJANGO_SUPERUSER_PASSWORD" ] ; then
    (cd /opt/app/website/; python manage.py createsuperuser --no-input)
fi
echo $PWD
# (cd ./website/; gunicorn mysite.wsgi --preload --bind 127.0.0.1:8010 --workers 3) &
(cd /opt/app/website/deploy; gunicorn --bind 127.0.0.1:8010 mysite.wsgi:application) &
nginx -g "daemon off;"