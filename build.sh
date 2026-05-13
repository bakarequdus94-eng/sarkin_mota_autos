#!/usr/bin/env bash
# exit on error
set -o errexit

pip install -r requirements.txt

python manage.py collectstatic --no-input
python manage.py migrate
# This creates the superuser automatically using the environment variables above
python manage.py createsuperuser --noinput || true