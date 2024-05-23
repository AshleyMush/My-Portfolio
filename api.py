from flask import Flask, jsonify, request, Blueprint
from models import db, Projects
import os

api_app = Blueprint('api', __name__)

@api_app.route('/all', methods= ['GET'])
def get_all_projects():
    all_projects = Projects.query.all()
    return jsonify(projects = [ project.to_dict() for project in all_projects])