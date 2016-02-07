import datetime

from sqlalchemy import Column, ForeignKey, Integer, String, DateTime
from sqlalchemy import PrimaryKeyConstraint
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
 
Base = declarative_base()


class User(Base):
    __tablename__ = 'user'

    # SQL definitions
    id = Column(Integer, primary_key=True)
    name = Column(String(250), index=True, unique=True)

    # ORM definitions for simple access
    sessions = relationship("sensor_session", back_populates='user')


class SensorSession(Base):
    __tablename__ = 'sensor_session'

    # SQL definitions
    id = Column(Integer, primary_key=True)
    created = Column(DateTime, default=datetime.datetime.now())
    # or Column(DateTime, default=datetime.datetime.now) - defers time a bit
    user_id = Column(Integer, ForeignKey('user.id'))

    # ORM definitions for simple access
    user = relationship("user", back_populates='sensor_session')
    data = relationship("sensor_data", back_populates='sensor_session')


class SensorData(Base):
    __tablename__ = 'sensor_data'

    # SQL definitions
    session_id = Column(Integer, ForeignKey('sensor_session.id'))
    nano_time = Column(Integer)
    PrimaryKeyConstraint(session_id, nano_time)

    # ORM definitions for simple access
    session = relationship("sensor_session", back_populates='sensor_data')


engine = create_engine('sqlite:///:memory:', echo=True)
 
# Create tables
Base.metadata.create_all(engine)
print(datetime.datetime.now())