from sqlalchemy import Integer, String, ForeignKey
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from datetime import date

# declarative base class
class Base(DeclarativeBase):
    pass


# an example mapping using the base
class UsaJobs(Base):
    __tablename__ = "usa_jobs"

    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str]
    position_uri: Mapped[str]
    apply_uri: Mapped[str]
    country: Mapped[str]
    region: Mapped[str]
    city: Mapped[str]
    organization_name: Mapped[str]
    department_name: Mapped[str]
    job_category: Mapped[str]
    qualification_summary: Mapped[str]
    renumeration_min: Mapped[float]
    renumeration_max: Mapped[float]
    application_start_date: Mapped[date]
    application_end_date: Mapped[date]
    requirements: Mapped[str]
    evaluations: Mapped[str]
    requiremed_documents: Mapped[str]
    relevance_rank: Mapped[int]


sql = '''
CREATE TABLE toggl.usa_jobs (
    id bigint PRIMARY KEY, -- MatchedObjectID
    title text, -- PositionTitle
    position_uri text, --PositionURI
    apply_uri text, --ApplyURI
    country text, --PositionLocation[0]['CountryCode']
    region text, --PositionLocation[0]['CountrySubDivisionCode']
    city text, --PositionLocation[0]['CityName']
    organization_name text, --OrganizationName
    department_name text,  --DepartmentName
    job_category text, --JobCategory[0]['Name']
    qualification_summary text, --QualificationSummary
    renumeration_min double, --PositionRenumeration[0]['MinimumRange']
    renumeration_max double, --PositionRenumeration[0]['MaximumRange']
    application_start date,  --ApplicationStartDate
    application_end date,    --ApplicationCloseDate
    requirements text,       --UserArea['Requirements']
    evaluations text,        --UserArea['Evaluations']
    required_documents,      --UserArea['RequiredDocuments']
    relevance_rank int       --RelevanceRank
)

'''