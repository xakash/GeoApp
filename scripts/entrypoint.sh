#!/bin/sh

set -e

python manage.py makemigrations
python manage.py migrate

python manage.py create-superuser \
                --username geoadmintest \
                --password geoadmintest \
                --email geoadmin@admin.com

echo "superuser created"