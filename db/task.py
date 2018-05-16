from sqlalchemy import Column, DateTime, String, Integer, create_engine, JSON, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import scoped_session, sessionmaker
import db.orm_handler as orm

class Task(orm.Base):
    __tablename__ = 'tasks'
    task_id = Column(String(100), primary_key=True)
    project_id = Column(String(100), ForeignKey('projects.project_id'))
    sequence = Column(Integer)
    content = Column(String(600))
