from api_data_fetcher import usa_jobs_api_fetcher as usa_jobs
from api_data_fetcher.utils import usa_jobs_api_key, get_conn


host = 'data.usajobs.gov'
user_agent = 'your@email.address'

headers = {
    "Host": host,
    "User-Agent": user_agent,
    "Authorization-Key": usa_jobs_api_key
}

url = f'https://data.usajobs.gov/api/Search?Page={page}&ResultsPerPage={result_per_page}&Keyword={keyword}'