from sqlalchemy import create_engine, Column, Integer, String
import os
engine = create_engine(os.getenv('DATABASE_URL'), echo=True)

from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base()

class Dog(Base):
   __tablename__ = 'dogs'
   id = Column(Integer, primary_key=True)
   name = Column(String)

Base.metadata.create_all(engine)