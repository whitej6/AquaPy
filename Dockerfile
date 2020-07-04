FROM python:3.7-slim

USER root

RUN apt update && \
    apt install -y i2c-tools \
                   libi2c-dev \
                   gcc \
                   libc-dev \
                   postgresql-client \
                   libpq-dev

COPY requirements.txt /tmp/requirements.txt

RUN pip install -r /tmp/requirements.txt

COPY aquapy/ /opt/aquapy/

WORKDIR /opt/aquapy

RUN ./manage.py collectstatic --noinput
