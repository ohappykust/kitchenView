FROM python:3.10-alpine

ARG DOCKER_TAG
ARG TZ=Europe/Moscow

ENV APP_VERSION ${DOCKER_TAG}
ENV TZ ${TZ}

WORKDIR /backend

RUN pip install --upgrade pip

RUN apk add gcc musl-dev libffi-dev
RUN apk add openssl=3.1.4-r6 --update

RUN pip install poetry && poetry config virtualenvs.create false

COPY . /backend

RUN poetry install --no-interaction

ENV PYTHONPATH=/backend
