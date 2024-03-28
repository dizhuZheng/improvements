from sqlalchemy import create_engine, Column, Integer, String
import os

engine = create_engine(os.getenv('DATABASE_URL'), echo=True)

from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base()

class User(Base):
   __tablename__ = 'users'
   id = Column(Integer, primary_key=True)
   name = Column(String)
   email = Column(String, unique=True)
   password = Column(String)

Base.metadata.create_all(engine)