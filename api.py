from flask import Flask, jsonify, request, abort, Blueprint
from models import db, Projects
import os

api_app = Blueprint('api', __name__)


#GET (READ all projects)
@api_app.route('/all', methods=['GET'])
def get_all_projects():

    all_projects = Projects.query.all()
    return jsonify(projects = [ project.to_dict() for project in all_projects])


#GET specific ID (Read this specific ID)
@api_app.route('/project/<int:id>', methods = ['GET'])
def get_project(id):
    project = Projects.query.get_or_404(id)
    if project is None:
        abort(404, description="Project not found")

    return jsonify(project.to_dict())


