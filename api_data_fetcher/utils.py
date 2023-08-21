import psycopg2
import os 
import requests


request_errors = (requests.exceptions.HTTPError, requests.exceptions.ConnectionError, 
                  requests.exceptions.Timeout, requests.exceptions.RequestException)

db_host = os.getenv('db_host')
db_pass = os.getenv('db_pass')
db_user = os.getenv('db_user')
db_port = os.getenv('db_port')
db_name = os.getenv('db_name')
usa_jobs_api_key = os.getenv('usa_jobs_api_key')

def get_conn():
    return psycopg2.connect(host=db_host, 
                            port=db_port, 
                            user=db_user, 
                            database=db_name, 
                            password=db_pass)

def safe_get(data, *keys):
    '''
    Access @*keys in nested @data dictionary and return `None` instead of `KeyError`.
    '''
    val = data
    for key in keys:
        if val is None:
            return
        try:
            val = val[key]
        except (TypeError, IndexError, KeyError):
            val = None
    return val


