set -o errexit

pip install poetry
poetry install

cd /opt/render/project/src/test_stripe/src
python manage.py collectstatic --no-input
python makemigrations
python manage.py migrate