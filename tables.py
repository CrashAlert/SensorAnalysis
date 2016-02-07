import datetime

from sqlalchemy import Column, ForeignKey, Integer, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
 
Base = declarative_base()


class User(Base):
    __tablename__ = 'user'

    id = Column(Integer, primary_key=True)
    name = Column(String(250))


class SensorSession(Base):
    __tablename__ = 'sensor_session'

    id = Column(Integer, primary_key=True)
    created = Column(DateTime, default=datetime.datetime.utcnow)

    user_id = Column(Integer, ForeignKey('user.id'))
    user = relationship(User)


class SensorData(Base):
    __tablename__ = 'sensor_data'

    id = Column(Integer, primary_key=True)

    session_id = Column(Integer, ForeignKey('sensor_session.id'))
    session = relationship(SensorSession)


engine = create_engine('sqlite:///:memory:', echo=True)
 
# Create tables
Base.metadata.create_all(engine)