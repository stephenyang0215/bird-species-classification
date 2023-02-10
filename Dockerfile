From python:3.8.10

WORKDIR /app
COPY . /app

RUN pip install --upgrade pip
RUN apt-get update \
    && apt-get -y install libpq-dev gcc
RUN pip install -r requirements.txt

CMD ["streamline", "run", "--server.enableCORS", "true", "app.py"]