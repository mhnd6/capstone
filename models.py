from sqlalchemy import Column, String, create_engine, Integer
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import json
import os

# set my environment variables
# os.environ['DATABASE_PATH'] = 'postgres://xvghnwhkvpsmum:9c510ebc2170457c8eac775fa5a7505bc1844ebf3b7450142846152010454a80@ec2-184-73-249-9.compute-1.amazonaws.com:5432/ddfamoh8uvbp4p'
database_path = os.environ.get('DATABASE_PATH')
print(database_path, flush=True)
db = SQLAlchemy()
migrate = Migrate()

'''
setup_db(app)
    binds a flask application and a SQLAlchemy service
'''


def setup_db(app, database_path=database_path):
    app.config["SQLALCHEMY_DATABASE_URI"] = database_path
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    db.app = app
    db.init_app(app)
    migrate.init_app(app, db)
    db.create_all()


'''
Movies
a persistent Movies entity, extends the base SQLAlchemy Model
'''


class Movies(db.Model):
    __tablename__ = 'movies'
    id = Column(Integer, primary_key=True)
    title = Column(String(400), nullable=False)
    release_date = Column(String(100))

    def __init__(self, title, release_date):
        self.title = title
        self.release_date = release_date

    '''
    insert()
        inserts a new model into a database
        EXAMPLE
            movie = Movies(title=req_title, release_date=req_recipe)
            movie.insert()
    '''

    def insert(self):
        db.session.add(self)
        db.session.commit()

    '''
    update()
        updates a new model into a database
        EXAMPLE
            movie = Movies.query.get(2)
            movie.title = 'Hi'
            movie.update()
    '''

    def update(self):
        db.session.commit()

    '''
    delete()
        deletes a new model into a database
        EXAMPLE
            movie = Movies.query.get(2)
            movie.delete()
    '''

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def format(self):
        return {
            "id": self.id,
            "title": self.title,
            "release_date": self.release_date

        }


'''
Actors
a persistent Actors entity, extends the base SQLAlchemy Model
'''


class Actors(db.Model):
    __tablename__ = 'actors'
    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    age = Column(Integer)
    gender = Column(String)

    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    '''
    insert()
        inserts a new model into a database
        EXAMPLE
            actor = Actors(name=ahmed, age=50, gender=male)
            actor.insert()
    '''

    def insert(self):
        db.session.add(self)
        db.session.commit()

    '''
    update()
        updates a new model into a database
        EXAMPLE
            actor = Actors(name=ahmed, age=50, gender=male)
            actor.update()
    '''

    def update(self):
        db.session.commit()

    '''
    delete()
        deletes a new model into a database
        EXAMPLE
            actor = Actors.query.get(2)
            actor.delete()
    '''

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def format(self):
        return {
            "id": self.id,
            "name": self.name,
            "age": self.age,
            "gender": self.gender

        }
