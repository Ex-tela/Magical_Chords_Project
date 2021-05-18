FROM python:3.6-alpine

COPY . /code
WORKDIR /code

CMD ["python","chord_server.py" ]