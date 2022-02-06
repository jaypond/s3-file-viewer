FROM python:3.8-slim-buster

COPY ./deployment/requirements.txt .
RUN pip3 install -r ./requirements.txt