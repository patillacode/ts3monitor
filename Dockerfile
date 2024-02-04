FROM python:3.11-slim-buster

RUN apt-get update && apt-get install -y make gcc curl
RUN mkdir ts3monitor

COPY . /ts3monitor

WORKDIR /ts3monitor

RUN pip install -r requirements.txt

