until PGPASSWORD=$db_pass psql -h "$db_host" -U "$db_user" -d "$db_name" -p ${db_port} -c '\q'; do
  >&2 echo "PostgreSQL is unavailable - sleeping"
  sleep 1
done

PGPASSWORD=$db_pass psql -U ${db_user} -h ${db_host} -p ${db_port} -d ${db_name} -c "SELECT 1 FROM pg_tables WHERE tablename = 'usa_jobs';"

if [ $? -eq 0 ]; then
    echo "Tables exist .."
    alembic upgrade head
else
    alembic revision --autogenerate -m "Create usa_jobs table"
    alembic upgrade head

fi

output=$(PGPASSWORD=$db_pass psql -U "${db_user}" -h "${db_host}" -p "${db_port}" -d "${db_name}" -c "SELECT count(*) FROM usa_jobs LIMIT 10;" -t)

if [ $? -eq 0 ] && [ "$output" -gt 0 ]; then
    echo "The table usa_jobs already has data, skipping initial data ingestion pipeline."
else
    echo "The table usa_jobs is empty."
    echo "Starting data ingestion pipeline"
    python /app/api_data_fetcher/main.py
fi


