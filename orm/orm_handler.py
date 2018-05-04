from sqlalchemy import Column, DateTime, String, Integer, create_engine, JSON, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import scoped_session, sessionmaker

import config
import datetime

Base = declarative_base()

def _get_date():
    return datetime.datetime.now()

def init_db(uri=config.DB_URI):
    engine = create_engine(uri, convert_unicode=True)
    db_session = scoped_session(sessionmaker(autocommit=False, autoflush=False, bind=engine))
    Base.query = db_session.query_property()
    Base.metadata.drop_all(engine) 
    Base.metadata.create_all(bind=engine)
    return db_session
