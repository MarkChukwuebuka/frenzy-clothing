#!/bin/sh

echo "Waiting for PostgreSQL..."

while ! nc -z $PGHOST $PGPORT; do
    sleep 1
done

echo "PostgreSQL started."

python manage.py migrate --noinput

python manage.py collectstatic --noinput

exec "$@"
