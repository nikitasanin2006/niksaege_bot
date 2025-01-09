import os.path
from sqlalchemy import create_engine, Column, Integer, Text
#from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, declarative_base



# Первый параметр - класс (9, 11, 13), второй параметр - уровень подготовки (0, 50, 100), третий параметр - длина суммаризации (1, 2, 4)
Base = declarative_base()

class Users(Base):
    __tablename__= "Users"

    id = Column(Integer, primary_key=True)
    klass = Column(Integer)
    level = Column(Integer)
    width = Column(Integer)

class Data(Base):
    __tablename__ = "Data"

    id = Column(Integer, primary_key=True)
    oobe = Column(Integer, nullable=False)
    error = Column(Integer, nullable=False)


engine = create_engine('sqlite:///users.db', echo=False)
Session = sessionmaker(bind=engine)
session = Session()

Base.metadata.create_all(engine)
