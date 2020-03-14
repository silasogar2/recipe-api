FROM python:3.7-alpine
MAINTAINER Silas Ogar

ENV PYTHONUNBUFFERED 1

# Install dependencies
COPY ./requirements.txt /requirements.txt
RUN pip install -r /requirements.txt

# Setup directory structure
RUN mkdir /app
WORKDIR /app
COPY ./app /app

RUN adduser -D user
RUN chown user:user -R /app/
USER user