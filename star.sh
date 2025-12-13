#!/bin/bash
python manage.py migrate --noinput
python manage.py collectstatic --noinput
exec gunicorn ecocraft.wsgi:application --bind 0.0.0.0:$PORT