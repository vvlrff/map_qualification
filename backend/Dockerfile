FROM python:3.11-slim-buster as backend
COPY ../backend/requirements.txt /app/requirements.txt
RUN pip install -r /app/requirements.txt
RUN apt-get update

FROM backend

COPY ../backend /app/backend
COPY ../shared /app/shared

ENV PYTHONPATH "${PYTHONPATH}:/app"
WORKDIR /app/backend
