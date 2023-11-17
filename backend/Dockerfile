FROM python:3.11.3

WORKDIR /backend

COPY ./requirements.txt .
RUN pip install -r requirements.txt

COPY . .
RUN chmod a+x docker/*.sh