FROM python:3.9.5-slim-buster

ENV CHORDS_ENV=docker
RUN apt-get update && apt-get install -y libpq-dev gcc
COPY requirements.txt /req/
RUN pip install -r /req/requirements.txt 

COPY scripts /scripts/
RUN chmod +x /scripts/serve_flask_app.sh

COPY src /code/
WORKDIR /code/

CMD ["/scripts/serve_flask_app.sh" ]