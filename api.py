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

name  = "test project",
homepage_thumbnail  = " https://img.freepik.com/free-vector/business-idea-generation-plan-development-pensive-man-with-lightbulb-cartoon-character-technical-mindset-entrepreneurial-mind-brainstorming-process_335657-2104.jpg?t=st=1716841715~exp=1716845315~hmac=ca0fc8ce26b202f76576748a6a86f23bc04a0192568fdae976a4907d2591b448&w=826  ",
video_url  = " https://youtu.be/J5baELvIYds?si=rxq1AScAtLDSBe0m" 
category = " Machine Learning" ,
tech_used  = "Pandas, numpy, Matlab, Scikit Learn, Tableu,",
project_url  = "https://github.com/Example Project",
description = "This is an amazing example"



"""



