# encoding: utf-8
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import Numeric
from sqlalchemy import String
from sqlalchemy import Date
from sqlalchemy import Time
from sqlalchemy import DateTime
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship

Base = declarative_base()

class Event(Base):
    __tablename__ = 'livelihood_event'

    # columns
    id = Column('event_serial_number', Integer, primary_key=True)
    gov_sn = Column('government_serial_number', String)
    type = Column('event_type', String)
    city = Column('city', String)
    district = Column('district', String)
    road = Column('road_section', String)
    detail_addr = Column('lane_alley_number', String)
    start_date = Column(Date)
    end_date = Column(Date)
    start_time = Column(Time)
    end_time = Column(Time)
    description = Column(String)
    update_time = Column(DateTime)
    update_status = Column(Integer)

    # relationships
    areas = relationship('Area', back_populates='event')

class Area(Base):
    __tablename__ = 'group'

    # columns
    id = Column('group_id', Integer, primary_key=True)
    event_id = Column(Integer, ForeignKey('livelihood_event.event_serial_number'))

    # relationships
    event = relationship('Event', back_populates='areas')
    coordinates = relationship('Coordinate', back_populates='area')

class Coordinate(Base):
    __tablename__ = 'coordinate'

    # columns
    id = Column('coordinate_id', Integer, primary_key=True)
    twd97_x = Column('x', Numeric)
    twd97_y = Column('y', Numeric)
    area_id = Column(Integer, ForeignKey('group.group_id'))

    # relationships
    area = relationship('Area', back_populates='coordinates')
