import psycopg2

import os 

db_host = os.getenv('db_host')
db_pass = os.getenv('db_pass')
db_user = os.getenv('db_user')
db_port = os.getenv('db_port')
db_name = os.getenv('db_name')
usa_jobs_api_key = os.getenv('usa_jobs_api_key')


print("HOOOOST", db_host)
def get_conn():
    print("HOOOOST", db_host)
    return psycopg2.connect(host=db_host, port=db_port, user=db_user, database=db_name, password=db_pass)

