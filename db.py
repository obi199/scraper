from sqlalchemy import Column, Integer, String
from sqlalchemy.engine import create_engine
#from sqlalchemy.sql.expression import true
from sqlalchemy.ext.declarative import declarative_base

database= r"sqlite:///db"

engine = create_engine(database, echo=True)
Base = declarative_base()

class record(Base):
   __tablename__ = 'record'
   id = Column(Integer, primary_key = True)
   artist = Column(String)
   album = Column(String)
   track = Column(String)
   label = Column(String)
   year = Column(String)


Base.metadata.create_all(engine)
