FROM python:3.9

WORKDIR /app 

COPY requirements.txt /app/ 
RUN pip install -r requirements.txt 

COPY . /app

RUN apt-get update && \
    apt-get install -y postgresql-client && \
    rm -rf /var/lib/apt/lists/*

RUN apt-get update && apt-get -y install cron
RUN crontab cron-schedules/cron.txt


CMD [ "python" "api_data_fetcher/main.py" ]
