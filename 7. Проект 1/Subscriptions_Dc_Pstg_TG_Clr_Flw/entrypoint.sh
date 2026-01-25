#!/bin/sh
set -e

echo "Waiting for PostgreSQL..."
while ! nc -z database 5432; do
  sleep 0.5
done
echo "PostgreSQL started"

echo "Applying migrations..."
python manage.py migrate

echo "Creating superuser if needed..."
python manage.py shell << 'EOF'
from subscriptions.models import CustomUser
if not CustomUser.objects.filter(username='admin').exists():
    CustomUser.objects.create_superuser(
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

echo "Starting Django DRF server..."
exec "$@"