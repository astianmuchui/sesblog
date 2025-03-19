#!/usr/bin/env bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt

source venv/bin/activate
pip install django djangorestframework
python3 manage.py makemigrations --noinput
python3 manage.py migrate --noinput

python3 manage.py collectstatic --noinput