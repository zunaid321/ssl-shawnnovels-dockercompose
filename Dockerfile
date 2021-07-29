FROM ubuntu:20.04

RUN pip install --upgrade pip

RUN apt-get update && apt-get -y install libpq-dev gcc && pip install psycopg2

COPY ./requirements.txt .
RUN pip3 install -r requirements.txt

COPY ./django_project /app

WORKDIR /app

COPY ./entrypoint.sh /
ENTRYPOINT ["sh", "/entrypoint.sh"]

