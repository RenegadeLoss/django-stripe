FROM python:3.11


# Configure Poetry
ENV POETRY_HOME=/opt/poetry
ENV POETRY_VENV=/opt/poetry-venv
ENV POETRY_CACHE_DIR=/opt/.cache

# Install poetry separated from system interpreter
RUN python3 -m venv $POETRY_VENV \
    && $POETRY_VENV/bin/pip install -U pip setuptools \
    && $POETRY_VENV/bin/pip install poetry

# Add `poetry` to PATH
ENV PATH="${PATH}:${POETRY_VENV}/bin"
ENV POETRY_SECRET_KEY="django-insecure-+a1tnyrs4-5qs*xibavdl#y_1(10jksxn1qzz@k*!0^!61g+p="

WORKDIR /app

COPY . .

RUN poetry install
