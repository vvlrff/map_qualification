FROM python:3.11-slim-buster as alembic_base
COPY ../alembic/requirements.txt /app/requirements.txt
RUN pip install -r /app/requirements.txt

FROM alembic_base
COPY ../backend /app/backend
COPY ../alembic /app/alembic
COPY ../alembic.ini /app

ENV PYTHONPATH "${PYTHONPATH}:/app"

WORKDIR /app
