from flask import Flask, abort, render_template, redirect, url_for, flash, request, send_from_directory
from flask_bootstrap import Bootstrap5
from datetime import datetime
from flask_ckeditor import CKEditor
import smtplib
from email.mime.text import MIMEText
import smtplib
import os
from forms import ContactForm, LoginForm
from models import db, Projects
from api import api_app
import requests
import json

MY_EMAIL_ADDRESS = os.environ.get("EMAIL_KEY")
MY_EMAIL_APP_PASSWORD = os.environ.get("PASSWORD_KEY")

app = Flask(__name__)
app.config['SECRET_KEY'] = os.environ.get("SECRET_APP_KEY")
ckeditor = CKEditor(app)
Bootstrap5(app)

# -----------------Configure DB-------------------------
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///Projects.db"
db.init_app(app)

with app.app_context():
    db.create_all()

# Register the API blueprint in app
app.register_blueprint(api_app, url_prefix='/api')


def all_projects_list():
    """

    :return: value of projects which is a list of dictionaries containing projects
    """
    response = requests.get(url="http://127.0.0.1:5002/api/all")
    data = response.json()

    return data['projects']


@app.route('/', methods=['GET', 'POST'])
def home():
    contact_form = ContactForm()
    login_form = LoginForm()
    current_year = datetime.now().year

    list_of_projects = all_projects_list()


    if contact_form.validate_on_submit() and contact_form.data:
        name, email, subject, message = contact_form.name.data, contact_form.email.data, contact_form.subject.data, contact_form.message.data

        print(f"{name, email, subject, message}")

        send_confirmation_email(name=name, email=email, subject=subject)
        send_email(name=name, subject=subject, email=email, message=message)

        return render_template('index.html', current_year=current_year, msg_sent=True, form=contact_form)

    return render_template('index.html', projects=list_of_projects, current_year=current_year, msg_sent=False,
                           login=False, form=contact_form, login_form=login_form, )


# Todo: Create instance of db and  pasrse  projects to projects.html
@app.route('/projects', methods=['GET', 'POST'])
def all_projects():
    # Call the API endpoint
    response = requests.get(url="http://127.0.0.1:5002/api/all")
    data = response.json()
    list_of_projects = data['projects']

    return render_template('all-projects.html', projects=list_of_projects)


# HTTP- Create item
#Todo: create new project instance
#Todo: Change the instance variables to a dict
# Todo: use requests to post it
# Todo: Redirect to url_for( 'All_projects

@app.route('/add', methods=[ 'POST'])
def add_project():
    if request.method == 'POST':
        new_project = {
            'name': request.form.get('name'),
            'homepage_thumbnail': request.form.get('homepage_thumbnail'),
            'img_url': request.form.get('img_url'),
            'video_url': request.form.get('video_url'),
            'category': request.form.get('category'),
            'tech_used': request.form.get('tech_used'),
            'project_url': request.form.get('project_url'),
            'description': request.form.get('description')
        }
        response = requests.post(url="http://127.0.0.1:5002/api/insert-to-db", data=new_project)
        if response.status_code == 201:
            return redirect(url_for('all_projects'))
        else:
            return f"Error: Could not add project {new_project['name']}"
    return render_template('add_project.html')

    # @app.route('/fix/<int:id>', methods=['PATCH'])
    # def patch_to_api(id):
    #     params = request.args.to_dict()
    #     print(params)
    #     requests.patch(url=f"http://127.0.0.1:5002/api/patch/{id}", json=params)
    #
    #     if response.status_code == 200:
    #         return redirect(url_for('all_projects'))
    #     else:
    #         return f"Error: Could not update project {id}"
















# HTTP -Get a specific item
@app.route('/<int:id>', methods=['GET'])
def get_project(id):
    login_form = LoginForm()
    form = ContactForm()
    current_year = datetime.now().year

    list_of_projects = all_projects_list()


#TODO: Get projects from api
    response = requests.get(url=f'http://127.0.0.1:5002/api/project/{id}')
    data   = response.json()
    project = data



    if form.validate_on_submit() and form.data:
        name, email, subject, message = form.name.data, form.email.data, form.subject.data, form.message.data

        print(f"{name, email, subject, message}")

        send_confirmation_email(name=name, email=email, subject=subject)
        send_email(name=name, subject=subject, email=email, message=message)

        return render_template('base-project.html',project = project, current_year=current_year, msg_sent=True, form=form
                            , projects=list_of_projects, login_form=login_form)

    return render_template('base-project.html', project = project,current_year=current_year, msg_sent=False, form=form,
                           projects=list_of_projects, login_form=login_form)


@app.route('/download', methods=['GET', 'POST'])
def download():
    return send_from_directory('static', path="files/CV.pdf", as_attachment=True)


def send_confirmation_email(name, email, subject, service='gmail'):
    # Email content
    email_content = render_template('thanks.html', name=name)

    # MIMEText logic
    msg = MIMEText(email_content, 'html')
    msg['From'] = MY_EMAIL_ADDRESS
    msg['To'] = email  # Send to the user's email
    msg['Subject'] = f"Confirmation: {subject}"
    msg['Reply-To'] = MY_EMAIL_ADDRESS

    # ---SMTP logic-----

    smtp_settings = {
        'gmail': ('smtp.gmail.com', 587),
        'yahoo': ('smtp.mail.yahoo.com', 587),
        'outlook': ('smtp.office365.com', 587)
        # Add more services as needed
    }

    if service in smtp_settings:
        smtp_server, smtp_port = smtp_settings[service]
    else:
        raise ValueError("Unsupported email service")

    try:
        with smtplib.SMTP(smtp_server, smtp_port) as connection:
            connection.starttls()
            connection.login(MY_EMAIL_ADDRESS, MY_EMAIL_APP_PASSWORD)
            connection.sendmail(MY_EMAIL_ADDRESS, email, msg.as_string())
    except Exception as e:
        print(f"Error sending email: {e}")
        render_template('index.html')


def send_email(name, subject, email, message, service='gmail'):
    email_content = render_template('email-template.html', name=name, subject=subject, email=email,
                                    message=message)

    # -- MIMETEXT logic ---

    msg = MIMEText(email_content, 'html')
    msg['From'] = email
    msg['To'] = MY_EMAIL_ADDRESS
    msg['Subject'] = f"New message from {name}: {subject}"
    msg['Reply-To'] = email

    # ---SMTP logic-----

    smtp_settings = {
        'gmail': ('smtp.gmail.com', 587),
        'yahoo': ('smtp.mail.yahoo.com', 587),
        'outlook': ('smtp.office365.com', 587)
        # Add more services as needed
    }

    if service in smtp_settings:
        smtp_server, smtp_port = smtp_settings[service]
    else:
        raise ValueError("Unsupported email service")

    try:
        with smtplib.SMTP(smtp_server, smtp_port) as connection:
            connection.starttls()
            connection.login(MY_EMAIL_ADDRESS, MY_EMAIL_APP_PASSWORD)
            connection.sendmail(from_addr=email, to_addrs=MY_EMAIL_ADDRESS,
                                msg=msg.as_string())
    except Exception as e:
        print(f"Error sending email: {e}")
        render_template('index.html')


if __name__ == "__main__":
    app.run(debug=True, port=5002)
