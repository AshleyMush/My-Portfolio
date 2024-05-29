from flask import Flask, jsonify, request, abort, Blueprint
from models import db, Projects
import os

api_app = Blueprint('api', __name__)


# GET (READ all projects)
@api_app.route('/all', methods=['GET'])
def get_all_projects():
    projects = Projects.query.all()

    return jsonify(projects=[project.to_dict() for project in projects])


# GET specific ID (Read this specific ID)
@api_app.route('/project/<int:id>')
def get_project(id):
    project = Projects.query.get_or_404(id)

    return jsonify(project.to_dict())


#POST/ Create an entry - This is basically inserting data into our db
@api_app.route('/add', methods=['POST'])
def add_project():
    project_data = request.get_json()


    new_project = Projects(
        name=project_data['name'],
        homepage_thumbnail=project_data['homepage_thumbnail'],
        img_url=project_data['img_url'],
        video_url=project_data['video_url'],
        category=project_data['category'],
        tech_used=project_data['tech_used'],
        project_url=project_data['project_url'],
        description=project_data['description']
    )

    db.session.add(new_project)
    db.session.commit()

    return jsonify(message="Project added successfully"), 201



"""

name  = "Example project",
homepage_thumbnail  = " https://img.freepik.com/free-vector/idea-management-abstract-concept-illustration_335657-4878.jpg?t=st=1716961048~exp=1716964648~hmac=1456669674259e4e68b0ca32fb317e9da22d8ca02148737a69a9c5cf5572857e&w=740  ",
video_url  = "https://youtu.be/rSjt1E9WHaQ?si=ocTVz7eb80MrxpPu" 
category = " Web scraping" ,
tech_used  = "Node Js",
project_url  = "https://github.com/Example Project 1",
description = "WOW, amazing description"



"""



