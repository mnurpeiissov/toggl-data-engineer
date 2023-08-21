import requests
from utils import safe_get, request_errors
import time


def fetch_usajobs_data(url, headers, retries=3):
    errors = []
    response = None
    for _ in range(retries):
        try:
            response = requests.get(url, headers=headers)
            if response.status_code == 200:
                break
        except request_errors as ex:
            errors.append(ex)
            time.sleep(10)

    if response and response.status_code != 200:
        print(f'Could not fetch {url} with following errors: {errors}')

    return response.json() if response else {}

def build_job_json(response):
    '''
        build dict from response with required fields
    '''
    descriptor = response.get("MatchedObjectDescriptor")
    job_json = {
        "id": response.get("MatchedObjectId"), 
        "title": descriptor.get('PositionTitle'),
        "position_uri": descriptor.get("PositionURI"),
        "apply_uri": descriptor.get("ApplyURI"),
        "country": safe_get(descriptor, "PositionLocation", 0, "CountryCode"), 
        "region": safe_get(descriptor, "PositionLocation", 0, "CountrySubDivisionCode"),
        "city": safe_get(descriptor, "PositionLocation", 0 , "CityName"),
        "organization_name": descriptor.get("OrganizationName"),
        "department_name": descriptor.get("DepartmentName"),
        "job_category": safe_get(descriptor, "JobCategory", 0, "Name"),
        "qualification_summary": descriptor.get("QualificationSummary"),
        "remuneration_min": safe_get(descriptor, "PositionRemuneration", 0, "MinimumRange"),
        "remuneration_max": safe_get(descriptor, "PositionRemuneration", 0, "MaximumRange"),
        "application_start_date": descriptor.get("ApplicationStartDate"),
        "application_end_date": descriptor.get("ApplicationEndDate"),
        "requirements": safe_get(descriptor, "UserArea", "Requirements"),
        "evaluations": safe_get(descriptor, "UserArea", "Evaluations"),
        "required_documents": safe_get("UserArea", "RequiredDocuments"),            
        "relevance_rank": response.get("RelevanceRank")
    }
    return job_json


def persist_usajobs_data(cursor, job):
    '''
        Upsert the job, if it exists and there are changes it will update the existing job and if it does not
        exist, it will insert the new job
    '''
    cursor.execute('''
        INSERT INTO usa_jobs (id ,title, position_uri, apply_uri, country, region, city, organization_name,
                                    department_name, job_category, qualification_summary, remuneration_min,
                                    remuneration_max, application_start_date, application_end_date, requirements, 
                                    evaluations, required_documents, relevance_rank )
            SELECT 
                   %(id)s as id, 
                   %(title)s as title, 
                   %(position_uri)s as position_uri, 
                   %(apply_uri)s as apply_uri, 
                   %(country)s as country,
                   %(region)s as region, 
                   %(city)s as city, 
                   %(organization_name)s as organization_name, 
                   %(department_name)s as department_name, 
                   %(job_category)s as job_category,
                   %(qualification_summary)s as qualification_summary,
                   %(remuneration_min)s as remuneration_min,
                   %(remuneration_max)s as remuneration_max,
                   %(application_start_date)s as application_start_date,
                   %(application_end_date)s as application_end_date,
                   %(requirements)s as requirements, 
                   %(evaluations)s as evaluations,
                   %(required_documents)s as required_documents,
                   %(relevance_rank)s as relevance_rank
            ON CONFLICT(id) DO UPDATE SET 
                   title = EXCLUDED.title, 
                   position_uri = EXCLUDED.position_uri, 
                   apply_uri = EXCLUDED.apply_uri, 
                   country = EXCLUDED.country, 
                   region = EXCLUDED.region, 
                   city = EXCLUDED.city, 
                   organization_name = EXCLUDED.organization_name, 
                   department_name = EXCLUDED.department_name, 
                   job_category = EXCLUDED.job_category, 
                   qualification_summary = EXCLUDED.qualification_summary, 
                   remuneration_min = EXCLUDED.remuneration_min, 
                   remuneration_max = EXCLUDED.remuneration_max, 
                   application_start_date = EXCLUDED.application_start_date, 
                   application_end_date = EXCLUDED.application_end_date, 
                   requirements = EXCLUDED.requirements, 
                   evaluations = EXCLUDED.evaluations, 
                   required_documents = EXCLUDED.required_documents, 
                   relevance_rank = EXCLUDED.relevance_rank
    ''', job)
