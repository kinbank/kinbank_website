#!/usr/bin/env bash
# start-server.sh
if [ -n "$DJANGO_SUPERUSER_USERNAME" ] && [ -n "$DJANGO_SUPERUSER_PASSWORD" ] ; then
    (cd website/; python manage.py createsuperuser --no-input)
fi
echo $PWD
(cd website/; gunicorn mysite.wsgi --preload --bind 0.0.0.0:8010 --workers 3) &
nginx -g "daemon off;"
