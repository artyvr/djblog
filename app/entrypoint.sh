#!/bin/sh

# Django migrate
python manage.py migrate

# Create Django superuser
if [ "$DJANGO_SUPERUSER_USERNAME" ]; then
  python manage.py createsuperuser --noinput --username "$DJANGO_SUPERUSER_USERNAME" --email $DJANGO_SUPERUSER_EMAIL
fi

# Collect Django static
python manage.py collectstatic --noinput

# Run Gunicorn
gunicorn djblog.wsgi --bind 0.0.0.0:8000

exec "$@"