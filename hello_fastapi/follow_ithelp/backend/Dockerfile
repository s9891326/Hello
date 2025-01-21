FROM python:3.10-slim

ENV PYTHONDONTWRITEBYTECODE 1

WORKDIR /usr/backend

COPY ./requirements.txt /usr/backend/requirements.txt

RUN pip install --no-cache-dir -r requirements.txt

COPY . /usr/backend
