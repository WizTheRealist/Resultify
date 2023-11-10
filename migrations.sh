#!/usr/bin/env bash


rm -r db.sqlite3 */migrations 2> /dev/null
python manage.py makemigrations RESULTIFYAPP && \
python manage.py migrate && \
python manage.py createsuperuser && \
python manage.py runserver
