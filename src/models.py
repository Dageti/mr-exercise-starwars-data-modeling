import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    
    id = Column(Integer, primary_key=True)
    username = Column(String, unique=True, nullable=False)
    firstname = Column(String, nullable=False)
    lastname = Column(String, nullable=False)
    email = Column(String, unique=True, nullable=False)
    password = Column(String, nullable=False)
    
    # relationships

    favorites = relationship('Favorite', back_populates='user')
    followers = relationship('Follower', back_populates='user_from', foreign_keys='Follower.user_from_id')


class Planet(Base):
    __tablename__ = 'planet'
    
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    climate = Column(String)
    terrain = Column(String)
    population = Column(Integer)


class Character(Base):
    __tablename__ = 'character'
    
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    birth_year = Column(String)
    gender = Column(String(20))
    species = Column(String)


class Vehicle(Base):
    __tablename__ = 'vehicle'
    
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    model = Column(String)
    manufacturer = Column(String)
    crew = Column(Integer)
    passengers = Column(Integer)


class Movie(Base):
    __tablename__ = 'movie'
    
    id = Column(Integer, primary_key=True)
    title = Column(String, nullable=False)
    release_date = Column(Integer)
    director = Column(String)
    producer = Column(String)
    episode_number = Column(Integer)


class Favorite(Base):
    __tablename__ = 'favorite'
    
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'))
    planet_id = Column(Integer, ForeignKey('planet.id'), nullable=True)
    character_id = Column(Integer, ForeignKey('character.id'), nullable=True)
    vehicle_id = Column(Integer, ForeignKey('vehicle.id'), nullable=True)
    movie_id = Column(Integer, ForeignKey('movie.id'), nullable=True)
    
    # relationships

    user = relationship('User', back_populates='favorites')
    planet = relationship('Planet')
    character = relationship('Character')
    vehicle = relationship('Vehicle')
    movie = relationship('Movie')


    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
