FROM python:3.9-alpine3.12

ARG ENVIRONMENT
ENV ENVIRONMENT=$ENVIRONMENT

RUN apk --no-cache add \
    bash \
    postgresql-dev \
    python3-dev \
    gcc \
    curl \
    build-base \
    && python -m pip install --upgrade pip

RUN curl -O https://raw.githubusercontent.com/vishnubob/wait-for-it/81b1373f17855a4dc21156cfe1694c31d7d1792e/wait-for-it.sh \
    && chmod +x /wait-for-it.sh

WORKDIR /negrucoin

COPY poetry.lock pyproject.toml /negrucoin/
COPY .pylintrc /negrucoin/

RUN pip install poetry
RUN poetry config virtualenvs.create false \
  && poetry install $(test "$ENVIRONMENT" == production && echo "--no-dev") --no-interaction --no-ansi

COPY docker /docker
COPY negrucoin /negrucoin

RUN mkdir /django_static
RUN chmod -R +x /docker/django/