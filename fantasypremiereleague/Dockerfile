FROM python:3.7.2-slim
MAINTAINER Keshab Budhathoky <kb4it.professional@gmail.com>

ENV PYTHONUNBUFFERED 1


RUN apt-get update \
    && apt-get install -y gcc python3-dev \
        libmariadbclient-dev-compat \
        mysql-client \
    && rm -rf /var/lib/opt/lists/*

WORKDIR /opt/

ADD . ./


RUN pip install --upgrade pip
RUN pip install -r requirements.txt
