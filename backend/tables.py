import datetime
import math

from sqlalchemy import Column, ForeignKey, Integer, String, DateTime, Float
from sqlalchemy import PrimaryKeyConstraint
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
 
Base = declarative_base()


class User(Base):
    __tablename__ = 'user'

    # SQL definitions
    id = Column(Integer, primary_key=True)
    name = Column(String)#(250), index=True, unique=True)

    def __repr__(self):
        return '(%s) %s' % (str(self.id), self.name)


class SensorSession(Base):
    __tablename__ = 'sensor_session'

    # SQL definitions
    id = Column(Integer, primary_key=True)
    description = Column(String(250))
    created = Column(DateTime, default=datetime.datetime.now)
    user_id = Column(Integer, ForeignKey('user.id'))

    # ORM definitions for simple access
    user = relationship(User)

    def __repr__(self):
        return '(%s) created %s by %s' \
               % (str(self.id), str(self.created), str(self.user))


class SensorData(Base):
    __tablename__ = 'sensor_data'

    # SQL definitions
    # Keys
    session_id = Column(Integer, ForeignKey('sensor_session.id'))
    nano_time = Column(Integer)
    PrimaryKeyConstraint(session_id, nano_time)
    # Sensor recordings
    acc_x     = Column(Float, nullable=True)
    acc_y     = Column(Float, nullable=True)
    acc_z     = Column(Float, nullable=True)
    lin_acc_x = Column(Float, nullable=True)
    lin_acc_y = Column(Float, nullable=True)
    lin_acc_z = Column(Float, nullable=True)
    gyr_x     = Column(Float, nullable=True)
    gyr_y     = Column(Float, nullable=True)
    gyr_z     = Column(Float, nullable=True)
    rot_x     = Column(Float, nullable=True)
    rot_y     = Column(Float, nullable=True)
    rot_z     = Column(Float, nullable=True)
    mag_x     = Column(Float, nullable=True)
    mag_y     = Column(Float, nullable=True)
    mag_z     = Column(Float, nullable=True)
    lat       = Column(Float, nullable=True)
    lon       = Column(Float, nullable=True)
    bearing   = Column(Float, nullable=True)
    speed     = Column(Float, nullable=True)
    alt       = Column(Float, nullable=True)
    err_lat   = Column(Float, nullable=True)
    err_lon   = Column(Float, nullable=True)
    pressure  = Column(Float, nullable=True)
    station   = Column(Float, nullable=True)
    run       = Column(Float, nullable=True)
    walk      = Column(Float, nullable=True)
    auto      = Column(Float, nullable=True)
    cycling   = Column(Float, nullable=True)
    unknown   = Column(Float, nullable=True)

    # ORM definitions for simple access
    session = relationship(SensorSession)

    def __repr__(self):
        return '(%s, %s) of session %s' % \
               (str(self.session_id), str(self.nano_time), str(self.session))

    def acc(self):
        return math.sqrt(self.acc_x ** 2 + self.acc_y ** 2 + self.acc_z ** 2)
