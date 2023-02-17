set -o errexit

pip install poetry
poetry install

cd /opt/render/project/src
poetry run python manage.py collectstatic --no-input
poetry run python manage.py migrate