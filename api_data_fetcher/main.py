from usa_jobs_api_fetcher import persist_usajobs_data, build_job_json, fetch_usajobs_data
from utils import get_conn, usa_jobs_api_key

host = 'data.usajobs.gov'
user_agent = 'your@email.address'
headers = {
    "Host": host,
    "User-Agent": user_agent,
    "Authorization-Key": usa_jobs_api_key
}

page = 1 
result_per_page = 500
keyword = "Data Engineering"
processed = 0 

if __name__ == '__main__':
    conn = get_conn()
    with conn.cursor() as cursor:
        while True:
            print(f"Starting to process page number {page}")
            url = f'https://data.usajobs.gov/api/Search?Page={page}&ResultsPerPage={result_per_page}&Keyword={keyword}'
            data = fetch_usajobs_data(url, headers)
            if not data:
                print(f"There was no data for {url}")
                break
            print(f"len of data {len(data['SearchResult']['SearchResultItems'])}")
            for i, job in enumerate(data['SearchResult']['SearchResultItems']): 
                job_json = build_job_json(job)
                persist_usajobs_data(cursor, job_json)
            conn.commit()
            processed += len(data['SearchResult']['SearchResultItems'])
            print(f"INFO: processed page{page}")
            print(f"INFO: processed amount = {processed}")
            page += 1
            if processed >= data['SearchResult']['SearchResultCountAll']:
                print("FINISHED PROCESSING: ", processed)
                break