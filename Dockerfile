FROM python:3.6-alpine

COPY requirements.txt /req/
RUN pip install -r /req/requirements.txt 

COPY scripts /scripts/
RUN chmod +x /scripts/serve_flask_app.sh

COPY src /code/
WORKDIR /code/

CMD ["/scripts/serve_flask_app.sh" ]