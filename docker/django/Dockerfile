FROM python:3.9-alpine3.12

ARG ENVIRONMENT
ENV ENVIRONMENT=$ENVIRONMENT

RUN apk --no-cache add \
    bash \
    postgresql-dev \
    python3-dev \
    gcc \
    python3-dev \
    curl

RUN curl -O https://raw.githubusercontent.com/vishnubob/wait-for-it/81b1373f17855a4dc21156cfe1694c31d7d1792e/wait-for-it.sh \
    && chmod +x /wait-for-it.sh

WORKDIR /code

COPY requirements.txt /code/

RUN python -m pip install --upgrade pip
RUN python -m pip install -r requirements.txt

COPY docker /docker
COPY negrucoin /code

RUN mkdir /django_static
RUN chmod -R +x /docker/django/