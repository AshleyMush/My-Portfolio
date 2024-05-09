from flask_sqlalchemy import SQLAlchemy
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from flask_login import UserMixin


db = SQLAlchemy()


class Projects(db.Model):
    __tablename__ = "projects"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), unique=True, nullable=True)
    img_url = db.Column(db.String(250), unique=True, nullable= True)
    video_url = db.Column(db.String(250), unique=True, nullable= True)
    category = db.Column(db.String(250), nullable=True)
    tech_used = db.Column(db.String(250), nullable=True)
    project_url = db.Column(db.String(250), nullable=True, unique=True)
    description = db.Column(db.String(250), nullable=True)
