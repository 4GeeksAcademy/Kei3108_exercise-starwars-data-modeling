import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Character(Base):
    __tablename__ = 'characters'
    ID = Column(Integer, primary_key=True)
    Name = Column(String(20))
    Height = Column(Integer)
    Mass = Column(Integer)
    HairColor = Column(String(20))
    Planet_ID = Column(Integer, ForeignKey('planets.ID'))
    Vehicle_ID = Column(Integer, ForeignKey('vehicles.ID'))

class Planet(Base):
    __tablename__ = 'planets'
    ID = Column(Integer, primary_key=True)
    Name = Column(String(20))
    Diameter = Column(Integer)
    Rotation = Column(Integer)
    Terrain = Column(String(20))

class Vehicle(Base):
    __tablename__ = 'vehicles'
    ID = Column(Integer, primary_key=True)
    Name = Column(String(20))
    Manufacturer = Column(String(20))
    Cost_in_credits = Column(Integer)
    Length = Column(Integer)

class Favorite(Base):
    __tablename__ = 'favorites'
    ID = Column(Integer, primary_key=True)
    Character_ID = Column(Integer, ForeignKey('characters.ID'))
    Vehicle_ID = Column(Integer, ForeignKey('vehicles.ID'))
    Planets_ID = Column(Integer, ForeignKey('planets.ID'))

class User(Base):
    __tablename__ = 'users'
    ID = Column(Integer, primary_key=True)
    Username = Column(String(20))
    Password = Column(String(20))
    Email = Column(String(50))
    Favorites_ID = Column(Integer, ForeignKey('favorites.ID'))

# Relationships
Character.Favorites = relationship("Favorite", back_populates="character")
Planet.Favorites = relationship("Favorite", back_populates="planet")
Vehicle.Favorites = relationship("Favorite", back_populates="vehicle")
Favorite.Character = relationship("Character", back_populates="Favorites")
Favorite.Planet = relationship("Planet", back_populates="Favorites")
Favorite.Vehicle = relationship("Vehicle", back_populates="Favorites")
User.Favorites = relationship("Favorite", back_populates="user")


def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
