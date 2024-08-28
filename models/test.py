from sqlalchemy import Column, String, Text, DateTime,Integer
from sqlalchemy.ext.declarative import declarative_base
import datetime
from models.base import Base

class Test(Base):
  __tablename__ = 'test'

  id = Column(Integer, primary_key=True)
  name = Column(String)
  description = Column(Text)
  created_at = Column(DateTime,default=datetime.datetime.now)
  updated_at = Column(DateTime)

  
