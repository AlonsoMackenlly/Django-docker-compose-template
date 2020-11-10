FROM python:3.8
MAINTAINER Alekseev Mikhail <alonso.mackenlly@gmail.com>
ENV PYTHONUNBUFFERED=1

RUN mkdir /code
RUN mkdir /code/app

WORKDIR /code/app

COPY . /code/app/

RUN pip install -r requirements.txt

ENTRYPOINT ["/code/app/entrypoint.sh"]
