FROM python:3.11-alpine
COPY requirements.txt /temp/requirements.txt
COPY djblog /djblog
COPY entrypoint.sh /djblog
WORKDIR /djblog
EXPOSE 8000
RUN pip install --no-cache-dir --upgrade -r /temp/requirements.txt
RUN adduser --disabled-password app
USER app