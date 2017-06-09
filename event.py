# encoding: utf-8
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import Float
from sqlalchemy import String
from sqlalchemy import Date
from sqlalchemy import Time
from sqlalchemy import DateTime
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship

Base = declarative_base()

class Event(Base):
    __tablename__ = 'event'

    # columns
    id = Column('event_id', String, primary_key=True)
    gov_sn = Column('gov_serial_number', String)
    type = Column('event_type', String)
    city = Column('city', String)
    district = Column('district', String)
    road = Column('road_street_boulevard_section', String)
    detail_addr = Column('lane_alley_number', String)
    start_date = Column(String)
    end_date = Column(String)
    start_time = Column(String)
    end_time = Column(String)
    description = Column(String)
    update_time = Column(DateTime)
    update_status = Column(String)

    # relationships
    areas = relationship('Area', back_populates='event')

    def to_dict(self):
        return {
                   'id': self.id,
                   'gov_sn': self.gov_sn,
                   'type': self.type,
                   'city': self.city,
                   'district': self.district,
                   'road': self.road,
                   'detail_addr': self.detail_addr,
                   'start_date': self.start_date,
                   'end_date': self.end_date,
                   'start_time': self.start_time,
                   'end_time': self.end_time,
                   'description': self.description,
                   'update_time': self.update_time,
                   'affected_areas': [a.to_dict() for a in self.areas]
               }

class Area(Base):
    __tablename__ = 'event_coord_group'

    # columns
    id = Column('group_id', String, primary_key=True)
    event_id = Column(String, ForeignKey('event.event_id'))

    # relationships
    event = relationship('Event', back_populates='areas')
    coordinates = relationship('Coordinate', back_populates='area')

    def to_dict(self):
        return {
                   'shape': 'point' if len(self.coordinates) == 1 else 'polygon',
                   'coordinates': [c.to_dict() for c in self.coordinates]
               }

class Coordinate(Base):
    __tablename__ = 'event_coordinate'

    # columns
    id = Column('coordinate_id', String, primary_key=True)
    twd97_x = Column('x_coordinate', Float)
    twd97_y = Column('y_coordinate', Float)
    area_id = Column('group_id', String, ForeignKey('event_coord_group.group_id'))

    # relationships
    area = relationship('Area', back_populates='coordinates')

    def to_dict(self):
        return {
                   'twd97_x': self.twd97_x,
                   'twd97_y': self.twd97_y
               }
