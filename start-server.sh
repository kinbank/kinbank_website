#!/usr/bin/env bash
# start-server.sh
if [ -n "$DJANGO_SUPERUSER_USERNAME" ] && [ -n "$DJANGO_SUPERUSER_PASSWORD" ] ; then
    (cd /opt/app/website/; python manage.py createsuperuser --no-input)
fi
echo $PWD
(cd /opt/app/website/; gunicorn mysite.wsgi --preload --bind 127.0.0.1:8020 --workers 3) &
nginx -g "daemon off;"
