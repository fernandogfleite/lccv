FROM python:3.10.1

ENV PYTHONUNBUFFERED 1

RUN apt-get update \
  && apt-get -y install netcat gcc postgresql \
  && apt-get clean

RUN pip install --upgrade pip

COPY ./requirements.txt /requirements.txt

RUN pip install -r requirements.txt

COPY  ./.env /.env
COPY ./core /core
COPY ./lccv /lccv
COPY ./manage.py /manage.py