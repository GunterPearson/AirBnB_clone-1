#!/usr/bin/python3
""" Place Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Table, Column, String, ForeignKey, Integer, Float
from sqlalchemy.orm import relationship


class Place(BaseModel, Base):
    """ A place to stay """
    __tablename__ = 'places'
    city_id = Column(String(60), ForeignKey('cities.id'), nullable=False)
    user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
    reviews = relationship('Review', cascade='all, delete', backref='place')
    name = Column(String(128), nullable=False)
    description = Column(String(1024))
    number_rooms = Column(Integer, default=0, nullable=False)
    number_bathrooms = Column(Integer, default=0, nullable=False)
    max_guest = Column(Integer, default=0, nullable=False)
    price_by_night = Column(Integer, default=0, nullable=False)
    latitude = Column(Float)
    longitude = Column(Float)
    amenity_ids = []
    """ Commenting ut task 10 code to see if we get green checks back"""
    metadata = Base.metadata
    place_amenity = Table('place_amenity',
                          metadata,
                          Column("place_id", String(60),
                                 ForeignKey("places.id"),
                                 primary_key=True,
                                 nullable=False),
                          Column("amenity_id", String(60),
                                 ForeignKey("amenities.id"),
                                 primary_key=True,
                                 nullable=False))
    amenities = relationship("Amenity", secondary='place_amenity',
                             viewonly=False, backref='places')

    @property
    def reviews(self):
        """Returns the list of review instances with stuff equals to
        the current stuff
        """
        from models.engine.file_storage import FileStorage
        fs = FileStorage.all(Review)
        review_list = []
        for key, value in fs.items():
            if value.place_id in value and self.id == value.place_id:
                '''Append City instances maybe fucked up here!!!'''
                review_list.append(value)
        return review_list

    @property
    def amenities(self):
        """ amenity_id getter
            Changed this last night to just return the amenity_ids list
        """
        return self.amenity_ids

    @amenities.setter
    def amenities(self, obj):
        '''Not sure what the parameters are here, probably value?'''
        from models.amenity import Amenity
        if type(obj) is Amenity:
            self.amenity_ids.append(obj.id)
            # or is it like this -> self.amenity_ids = obj.id
