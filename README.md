# toggl-data-engineer
Take Home Assignment For Data Engineering Position at Toggl

# Used Technologies
1) Postgres as database
2) Python
3) Alembic
4) Sqlalchemy
5) psycopg2
6) Docker

# How to run 
 You will need installed docker and docker-compose to run it locally

 `git clone https://github.com/mnurpeiissov/toggl-data-engineer.git`
 `cd toggl-data-engineer`
 `docker-compose up --build`

 This will:
 1) create a postgres database
 2) create `usa_jobs` table
 3) run initial data ingestion
 4) run cron on foreground
 5) run data ingestion script based on cron schedule

 Cron schedule can be adjust on `cron-schedules/crontab`

 