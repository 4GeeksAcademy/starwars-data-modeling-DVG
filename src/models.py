import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class Usuario(Base):
    __tablename__ = 'usuarios'
    id = Column(Integer, primary_key=True)
    username = Column(String, unique=True, nullable=False)
    password = Column(String, nullable=False)
    likes = relationship('Likes', back_populates='user')

class Likes(Base):
    __tablename__ = 'favoritos'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    planet_id = Column(Integer, ForeignKey('planets.uid'))
    character_id = Column(Integer, ForeignKey('people.uid'))
    starship_id = Column(Integer, ForeignKey('starships.uid'))
    vehicle_id = Column(Integer, ForeignKey('vehicles.uid'))
    film_id = Column(Integer, ForeignKey('films.uid'))
    user = relationship('Usuario', back_populates='likes')
    planet = relationship('Planet')
    character = relationship('Person')
    vehicle = relationship('Vehicle')
    starship = relationship('Starship')
    film = relationship('Film')

class Vehicle(Base):
    __tablename__ = 'vehicles'
    uid = Column(Integer, primary_key=True)
    name = Column(String)
    model = Column(String)
    vehicle_class = Column(String)
    manufacturer = Column(String)
    cost_in_credits = Column(String)
    films = Column(String, ForeignKey('films.uid'))
    pilots = Column(String, ForeignKey('people.uid'))

class Species(Base):
    __tablename__ = 'species'
    uid = Column(Integer, primary_key=True)
    name = Column(String)
    classification = Column(String)
    designation = Column(String)
    average_height = Column(String)
    average_lifespan = Column(String)
    hair_colors = Column(String)
    homeworld = Column(Integer, ForeignKey('planets.uid'))
    people = Column(String, ForeignKey('people.uid'))

class Film(Base):
    __tablename__ = 'films'
    uid = Column(Integer, primary_key=True)
    title = Column(String)
    episode_id = Column(Integer)
    director = Column(String)
    opening_crawl = Column(String)
    characters = Column(String, ForeignKey('people.uid'))
    planets = Column(String, ForeignKey('planets.uid'))
    starships = Column(String, ForeignKey('starships.uid'))
    vehicles = Column(String, ForeignKey('vehicles.uid'))
    species = Column(String, ForeignKey('species.uid'))

class Planet(Base):
    __tablename__ = 'planets'
    uid = Column(Integer, primary_key=True)
    diameter = Column(String)
    rotation_period = Column(String)
    population = Column(String)
    terrain = Column(String)
    name = Column(String)

class Starship(Base):
    __tablename__ = 'starships'
    uid = Column(Integer, primary_key=True)
    model = Column(String)
    starship_class = Column(String)
    manufacturer = Column(String)
    cost_in_credits = Column(String)
    length = Column(String)
    passengers = Column(String)
    pilots = Column(String, ForeignKey('people.uid'))
    name = Column(String)

class Person(Base):
    __tablename__ = 'people'
    uid = Column(Integer, primary_key=True)
    height = Column(String)
    mass = Column(String)
    hair_color = Column(String)
    skin_color = Column(String)
    birth_year = Column(String)
    gender = Column(String)
    name = Column(String)
    homeworld = Column(Integer, ForeignKey('planets.uid'))

def to_dict(self):
    return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
