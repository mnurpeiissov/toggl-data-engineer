import requests
from http_helpers import transport_errors
import time

# PositionTitle, PositionURI, PositionLocation, PositionRemuneration

def fetch_usajobs_data(url, headers, retries=3):
    errors = []
    response = None
    for _ in range(retries):
        try:
            response = requests.get(url, headers=headers)
            if response.status_code == 200:
                break
        except transport_errors as ex:
            errors.append(ex)
            time.sleep(10)

    if response and response.status_code != 200:
        print(f'Could not fetch {url} with following errors: {errors}')
    
    return response.json()

def build_job_json(response):
    descriptor = response.get("MatchedObjectDescriptor")
    job_json = {
        "id": response.get("MatchedObjectId"), 
        "title": descriptor.get('PositionTitle'),
        "position_uri": descriptor.get("PositionURI"),
        "apply_uri": descriptor.get("ApplyURI"),
        "country": descriptor.get("PositionLocation")[0].get("CountryCode"),
        "region": descriptor.get("PositionLocation")[0].get("CountrySubDivisionCode"),
        "city": descriptor.get("PositionLocation")[0].get("CityName"),
        "organization_name": descriptor.get("OrganizationName"),
        "department_name": descriptor.get("DepartmentName"),
        "job_category": descriptor.get("JobCategory")[0].get("Name"),
        "qualification_summary": descriptor.get("QualificationSummary"),
        "renumeration_min": descriptor.get("PositionRenumeration")[0]["MinimumRange"],
        "renumeration_max": descriptor.get("PositionRenumeration")[0]["MaximumRange"],
        "application_start_date": descriptor.get("ApplicationStartDate"),
        "application_end_date": descriptor.get("ApplicationEndDate"),
        "requirements": descriptor.get("UserArea").get("Requirements"),
        "evaluations": descriptor.get("UserArea").get("Evaluations"),
        "required_documents": descriptor.get("UserArea").get("RequiredDocuments"),
        "relevance_rank": response.get("RelevanceRank")
    }
    return job_json





def persist_usajobs_data(cursor, job):
    cursor.execute('''
        INSERT INTO toggl.usa_jobs (id ,title, position_uri, apply_uri, country, region, city, organization_name,
                                    department_name, job_category, qualification_summary, renumeration_min,
                                    renumeration_max, application_start, application_end, requirements, 
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
                   %(renumeration_min)s as renumeration_min,
                   %(renumeration_max)s as renumeration_max,
                   %(application_start)s as application_start,
                   %(application_end)s as application_end,
                   %(requirements)s as requirements, 
                   %(evaluations)s as evaluations,
                   %(required_documents)s as required_documentsm 
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
                   renumeration_min = EXCLUDED.renumeration_min, 
                   renumeration_max = EXCLUDED.renumeration_max, 
                   application_start = EXCLUDED.application_start, 
                   application_end = EXCLUDED.application_end, 
                   requirements = EXCLUDED.requirements, 
                   evaluations = EXCLUDED.evaluations, 
                   required_documents = EXCLUDED.required_documents, 
                   relevance_rank = EXCLUDED.relevance_rank
    ''', job)