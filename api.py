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
def get_selected_project(id):
    project = Projects.query.get_or_404(id)

    return jsonify(project.to_dict())

#POST/ Create an entry - This is basically inserting data into our db
"""TODO:
request to get the json
Commit the new project 
return json  message of success  
"""
@api_app.route('/insert-to-db', methods=['POST'])
def add_project_to_db():
    try:
        # Extract data from the request
        project_data = request.get_json()

        # Create a new project with the provided data
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

        # Add the new project to the database
        db.session.add(new_project)
        db.session.commit()

        # Return a success message
        return jsonify(message="Project added successfully"), 201

    except Exception as e:
        # If there was an error, return an error message
        return jsonify(message=f"Error: Could not add project. Details: {str(e)}"), 400

#Patch (Update some of the data)

@api_app.route('/patch/<int:id>', methods=['PATCH'])
def patch_project(id):

    project_selected = Projects.query.get_or_404(id)
    query_params = request.args

    print(project_selected)
    print(type(query_params))
    print(query_params)

    if project_selected:
        for key, value in query_params.items():
            if hasattr(project_selected, key):
                setattr(project_selected, key, value)
            else:
                return jsonify(message=f"Key {key} not found in the project"), 404

        db.session.commit()
        return jsonify(message="Project updated successfully"), 200
    else:
        return jsonify(message="Project not found"), 404



@api_app.route('/Update/<int:id>', methods = ['PUT'])
def update_project(id):
    project_selected = Projects.query.get_or_404(id)
    update_data = request.get_json()

    if project_selected:
        project_selected.name = update_data.get('name', project_selected.name)
        project_selected.homepage_thumbnail = update_data.get('homepage_thumbnail', project_selected.homepage_thumbnail)
        project_selected.img_url = update_data.get('img_url', project_selected.img_url)
        project_selected.video_url = update_data.get('video_url', project_selected.video_url)
        project_selected.category = update_data.get('category', project_selected.category)
        project_selected.tech_used = update_data.get('tech_used', project_selected.tech_used)
        project_selected.project_url = update_data.get('project_url', project_selected.project_url)
        project_selected.description = update_data.get('description', project_selected.description)

        db.session.commit()
        return jsonify(message="Project updated successfully"), 200
    else:
        return jsonify(message="Project not found"), 404



@api_app.route('/delete-project/<int:id>', methods= ['Delete'])
def delete_project(id):
    selected_project = Projects.query.get_or_404(id)
    db.session.delete(selected_project)
    db.session.commit()
    return jsonify({'message': 'Project Deleted'})














