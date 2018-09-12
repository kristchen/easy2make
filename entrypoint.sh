#!/bin/sh
python /easy2make/health.py
python /easy2make/manage.py makemigrations --settings=easy2make.prod_settings
python /easy2make/manage.py migrate --settings=easy2make.prod_settings
python /easy2make/manage.py runserver 0.0.0.0:8000 --settings=easy2make.prod_settings

exec "$@"

