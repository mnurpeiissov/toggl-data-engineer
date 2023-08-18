if psql -U ${db_user} -h ${db_host} -p ${db_port} -d{db_name} -lqt | cut -d \| -f 1 | grep -qw toggl; then
    # database exists
    # $? is 0
    alembic revision --autogenerate -m "Create usa_jobs table"
else
    alembic revision --autogenerate -m "Create usa_jobs table"
fi