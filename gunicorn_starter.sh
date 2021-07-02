#!/bin/sh

cd /opt/app/website && gunicorn --bind 0.0.0.0:8010 mysite.wsgi:application