FROM python:3.9

WORKDIR /app 

COPY requirements.txt /app/ 
RUN pip install -r requirements.txt 
RUN apt-get update && \
    apt-get install -y postgresql-client && \
    rm -rf /var/lib/apt/lists/*

RUN apt-get update && apt-get -y install cron

COPY . /app
RUN crontab /app/cron-schedules/crontab
CMD ["cron", "-f"]
