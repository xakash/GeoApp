#!/bin/sh

set -e

python manage.py makemigrations
python manage.py migrate

python manage.py create-superuser \
                --username geoadmin \
                --password geoadmin \
                --email geoadmin@admin.com

echo "superuser created"