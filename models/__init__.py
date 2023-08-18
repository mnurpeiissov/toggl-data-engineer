import os

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from .usa_jobs import Base


db_url = os.environ.get("db_uri")
engine = create_engine(db_url, echo=False)
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)