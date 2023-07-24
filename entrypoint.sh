#!/bin/sh

python bin/manage.py migrate --no-input

python bin/manage.py collectstatic --no-input

gunicorn back_core.wsgi:application --bind 0.0.0.0:8000
