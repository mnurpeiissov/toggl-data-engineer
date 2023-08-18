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
