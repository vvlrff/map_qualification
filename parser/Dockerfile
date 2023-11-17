FROM python:3.11-slim-buster as parser_base
COPY ../parser/requirements.txt /app/requirements.txt
RUN pip install -r /app/requirements.txt

FROM parser_base

COPY ../parser /app/parser
COPY ../shared /app/shared
ENV PYTHONPATH "${PYTHONPATH}:/app"