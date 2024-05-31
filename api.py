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
"""TODO:
request to get the json
Commit the new project 
return json  message of success  
"""
@api_app.route('/insert-to-db', methods=['POST'])
def add_project():
    try:
        project_data = request.form
        new_project = Projects(
            name=project_data.get('name'),
            homepage_thumbnail=project_data.get('homepage_thumbnail'),
            img_url=project_data.get('img_url'),
            video_url=project_data.get('video_url'),
            category=project_data.get('category'),
            tech_used=project_data.get('tech_used'),
            project_url=project_data.get('project_url'),
            description=project_data.get('description')
        )
    except Exception as e:
        return jsonify(message=f"Project POSTING was unsuccessful: {e}"), 400

    db.session.add(new_project)
    db.session.commit()
    return jsonify(message="Project added successfully"), 201

# #Patch (Update some of the data)
# @api_app.route('/patch/<int:id>', methods=['PATCH'])
# def patch_project(id):
#     project= Projects.query.get_or_404(id)
#     update_data = request.get_json()
#     print(project)
#     for key, value in update_data.items():
#         setattr(Projects,key ,value)
#
#     db.session.commit()
#     return jsonify(message="Project updated successfully"), 200










