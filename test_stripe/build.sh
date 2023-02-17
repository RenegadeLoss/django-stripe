set -o errexit

pip install poetry
poetry install

cd /src
python manage.py collectstatic --no-input
python manage.py migrate