set -o errexit

pip install poetry
poetry install

cd /opt/render/project/src
python manage.py collectstatic --no-input
python manage.py migrate