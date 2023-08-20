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
    title: Mapped[str] = mapped_column(nullable=True)
    position_uri: Mapped[str] = mapped_column(nullable=True)
    apply_uri: Mapped[str] = mapped_column(nullable=True)
    country: Mapped[str] = mapped_column(nullable=True)
    region: Mapped[str] = mapped_column(nullable=True)
    city: Mapped[str] = mapped_column(nullable=True)
    organization_name: Mapped[str] = mapped_column(nullable=True)
    department_name: Mapped[str] = mapped_column(nullable=True)
    job_category: Mapped[str] = mapped_column(nullable=True)
    qualification_summary: Mapped[str] = mapped_column(nullable=True)
    renumeration_min: Mapped[float] = mapped_column(nullable=True)
    renumeration_max: Mapped[float] = mapped_column(nullable=True)
    application_start_date: Mapped[date] = mapped_column(nullable=True)
    application_end_date: Mapped[date] = mapped_column(nullable=True)
    requirements: Mapped[str] = mapped_column(nullable=True)
    evaluations: Mapped[str] = mapped_column(nullable=True)
    required_documents: Mapped[str] = mapped_column(nullable=True)
    relevance_rank: Mapped[int] = mapped_column(nullable=True)
