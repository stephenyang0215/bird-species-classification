#lightweight Python
FROM python:3.8-slim

RUN pip install --upgrade pip
RUN apt-get update \
    && apt-get -y install libpq-dev gcc

ENV APP_HOME /app
WORKDIR $APP_HOME
COPY . ./

RUN ls -la $APP_HOME/

#Install dependencies
RUN pip install -r requirements.txt

CMD ["streamlit", "run", "--server.enableCORS","true","app.py"]
