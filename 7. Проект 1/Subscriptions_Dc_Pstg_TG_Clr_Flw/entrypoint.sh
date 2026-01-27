#!/bin/sh
set -e

echo "Waiting for PostgreSQL..."
while ! nc -z database 5432; do
  sleep 0.1
done
echo "PostgreSQL started"

echo "Creating migrations..."
python manage.py makemigrations --noinput

echo "Applying migrations..."
python manage.py migrate --noinput

echo "Creating superuser if needed..."
python manage.py shell << 'EOF'
from django.contrib.auth import get_user_model
User = get_user_model()
if not User.objects.filter(username='admin').exists():
    User.objects.create_superuser(
        'admin',
        'admin@example.com',
        'Canada77',
        phone='+1234567890'
    )
    print('Superuser created successfully')
else:
    print('Superuser already exists')
EOF

echo "Collecting static files..."
python manage.py collectstatic --noinput

echo "Starting Gunicorn..."
exec gunicorn config.wsgi:application --bind 0.0.0.0:8000