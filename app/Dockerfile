FROM python:3.11-alpine
COPY requirements.txt /temp/requirements.txt
COPY djblog /djblog
WORKDIR /djblog
EXPOSE 8000
RUN apk add postgresql-client build-base postgresql-dev
RUN pip install --no-cache-dir --upgrade -r /temp/requirements.txt
RUN adduser --disabled-password app
USER app
