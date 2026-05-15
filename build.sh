#!/usr/bin/env bash
# exit on error
set -o errexit

pip install -r requirements.txt

python manage.py collectstatic --no-input
python manage.py migrate
# This creates the superuser automatically using the environment variables above
python manage.py shell <<EOF
from django.contrib.auth import get_user_model
User = get_user_model()
username = 'admin'
email = os.environ.get('DJANGO_SUPERUSER_EMAIL', 'bakarequdus94@gmail.com')
    password = os.environ.get('DJANGO_SUPERUSER_PASSWORD', 'your_default_secure_password')
if not User.objects.filter(username=username).exists():
    User.objects.create_superuser(username, email, password)
    print("Superuser created successfully")
else:
    user = User.objects.get(username=username)
    user.set_password(password)
    user.save()
    print("Superuser password updated successfully")
EOF