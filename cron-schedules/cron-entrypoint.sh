echo "starting cron"
crontab /app/cron-schedules/crontab
printenv | grep -v "no_proxy" >> /etc/environment
cron -f

