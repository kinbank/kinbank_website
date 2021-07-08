#!/bin/sh

# cd /opt/app/website && gunicorn --bind 0.0.0.0:$PORT mysite.wsgi:application
cd /opt/app/website && gunicorn --bind 0.0.0.0:8020 mysite.wsgi:application