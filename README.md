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


 # Deployment on the cloud
 There are various ways to deploy the pipeline in the cloud (I will consider Google Cloud Platform)
 1) Deploy on the VM. The most straighforward way is to deploy it on the cloud VM, which is very similary to running it locally
 2) Cloud Run and Cloud Scheduler
        * Create a Dockerfile that defines the environment and dependencies for your application.
        * Build your Docker image using the docker build command.
        * Push your Docker image to a container registry, such as Google Container Registry.
        * Create a Cloud Run service.
        * In the Cloud Run service configuration, specify the Docker image that you want to deploy.
        * Click Deploy.
        * Configure Cloud Scheduler with schedule and url of cloud run service
 3) GKE
        * Create a GKE cluster.
        * Create a Kubernetes Deployment (Cron Job) for your application.
        * In the Kubernetes Deployment configuration, specify the Docker image that you want to deploy.
        * Apply the Kubernetes Deployment.
