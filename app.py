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



@app.route('/', methods=['GET', 'POST'])
def home():
    contact_form = ContactForm()
    login_form = LoginForm()
    current_year = datetime.now().year
    projects = Projects.query.all()

    if contact_form.validate_on_submit() and contact_form.data:
        name, email, subject, message = contact_form.name.data, contact_form.email.data, contact_form.subject.data, contact_form.message.data

        print(f"{name, email, subject, message}")

        send_confirmation_email(name=name, email=email, subject=subject)
        send_email(name=name, subject=subject, email=email, message=message)

        return render_template('index.html', current_year=current_year, msg_sent=True, form=contact_form)

    return render_template('index.html', current_year=current_year, msg_sent=False, login =False, form=contact_form, login_form=login_form, projects=projects)

# Todo: Create instance of db and  pasrse  projects to projects.html
@app.route('/projects', methods=['GET', 'POST'])
def all_projects():
    projects = Projects.query.all()



    return render_template('all-projects.html', projects=projects)


@app.route('/add', methods=['GET', 'POST'])
def add_project():
    #Todo: Add form to add project and parse to db

    project1 = Projects(
        name=" Care Notes internal Audit tool.",
        homepage_thumbnail="https://img.freepik.com/free-vector/data-center-technology_24908-59337.jpg?t=st=1715633565~exp=1715637165~hmac=ea690113904429b4413e9cad42130c421d9b7ebf5f81d46267cc2f5a36f96fdb&w=740",
        img_url="https://img.youtube.com/vi/DJnH0jR8y5Q/maxresdefault.jpg",
        video_url="https://youtu.be/p9Q5a1Vn-Hk?si=-CtWc6FdrMhHRvU0",
        category="Python Desktop Application",
        tech_used="Python, pandas, numpy, Tkinter, selenium, OS lib",
    project_url="https://github.com/project1",
        description="A project that does something")

    project2 = Projects(
        name="Health Care Website",
        homepage_thumbnail="https://img.freepik.com/free-vector/online-purchases-from-home-3d-concepts-landing-page_52683-32652.jpg?t=st=1715634278~exp=1715637878~hmac=994cd8869d1729072d2b6f1a977ffb5f7253dce9d8f77da9b99fa48d1031d54a&w=1380",
        img_url="https://img.youtube.com/vi/DJnH0jR8y5Q/maxresdefault.jpg",
        video_url="https://youtu.be/DJnH0jR8y5Q",
        category="Full Stack Web App",
        tech_used="Python, flask with flask_wtf, boostrap, gunicord,  twilio API, SMTP lib, HHTP Requests",
        project_url="https://github.com/project2",
        description="A project that does something")

    db.session.add_all([project1, project2])
    db.session.commit()
    return redirect(url_for('all_projects'))





@app.route('/project/<int:id>', methods=['GET', 'POST'])
def project(id):
    form = ContactForm()
    current_year = datetime.now().year
    projects = Projects.query.all()

    project = Projects.query.get(id)

    if project is None:
        abort(404, description="Project not found")

    else:
        form = ContactForm()
        current_year = datetime.now().year

        if form.validate_on_submit() and form.data:
            name, email, subject, message = form.name.data, form.email.data, form.subject.data, form.message.data

            print(f"{name, email, subject, message}")

            send_confirmation_email(name=name, email=email, subject=subject)
            send_email(name=name, subject=subject, email=email, message=message)

            return render_template('base-project.html', current_year=current_year, msg_sent=True, form=form, project=project, projects=projects)

        return render_template('base-project.html', current_year=current_year, msg_sent=False, form=form, project=project, projects = projects)

    return redirect(url_for('home'))























@app.route('/project-1', methods=['GET', 'POST'])
def project1():

    form = ContactForm()
    current_year = datetime.now().year

    if form.validate_on_submit() and form.data:
        name, email, subject, message = form.name.data, form.email.data, form.subject.data, form.message.data

        print(f"{name, email, subject, message}")

        send_confirmation_email(name=name, email=email, subject=subject)
        send_email(name=name, subject=subject, email=email, message=message)

        return render_template('project-1.html', current_year=current_year, msg_sent=True, form=form)

    return render_template('project-1.html', current_year=current_year, msg_sent=False, form=form)


@app.route('/project-2', methods=['GET', 'POST'])
def project2():
    form = ContactForm()
    current_year = datetime.now().year

    if form.validate_on_submit() and form.data:
        name, email, subject, message = form.name.data, form.email.data, form.subject.data, form.message.data

        print(f"{name, email, subject, message}")

        send_confirmation_email(name=name, email=email, subject=subject)
        send_email(name=name, subject=subject, email=email, message=message)

        return render_template('project-2.html', current_year=current_year, msg_sent=True, form=form)

    return render_template('project-2.html', current_year=current_year, msg_sent=False, form=form)


@app.route('/project-3', methods=['GET', 'POST'])
def project3():
    form = ContactForm()
    current_year = datetime.now().year

    if form.validate_on_submit() and form.data:
        name, email, subject, message = form.name.data, form.email.data, form.subject.data, form.message.data

        print(f"{name, email, subject, message}")

        send_confirmation_email(name=name, email=email, subject=subject)
        send_email(name=name, subject=subject, email=email, message=message)

        return render_template('project-3.html', current_year=current_year, msg_sent=True, form=form)

    return render_template('project-3.html', current_year=current_year, msg_sent=False, form=form)


@app.route('/project-4', methods=['GET', 'POST'])
def project4():
    form = ContactForm()
    current_year = datetime.now().year

    if form.validate_on_submit() and form.data:
        name, email, subject, message = form.name.data, form.email.data, form.subject.data, form.message.data

        print(f"{name, email, subject, message}")

        send_confirmation_email(name=name, email=email, subject=subject)
        send_email(name=name, subject=subject, email=email, message=message)

        return render_template('project-4.html', current_year=current_year, msg_sent=True, form=form)

    return render_template('project-4.html', current_year=current_year, msg_sent=False, form=form)


@app.route('/project-5', methods=['GET', 'POST'])
def project5():
    form = ContactForm()
    current_year = datetime.now().year

    if form.validate_on_submit() and form.data:
        name, email, subject, message = form.name.data, form.email.data, form.subject.data, form.message.data

        print(f"{name, email, subject, message}")

        send_confirmation_email(name=name, email=email, subject=subject)
        send_email(name=name, subject=subject, email=email, message=message)

        return render_template('project-5.html', current_year=current_year, msg_sent=True, form=form)

    return render_template('project-5.html', current_year=current_year, msg_sent=False, form=form)


@app.route('/project-6', methods=['GET', 'POST'])
def project6():
    form = ContactForm()
    current_year = datetime.now().year

    if form.validate_on_submit() and form.data:
        name, email, subject, message = form.name.data, form.email.data, form.subject.data, form.message.data

        print(f"{name, email, subject, message}")

        send_confirmation_email(name=name, email=email, subject=subject)
        send_email(name=name, subject=subject, email=email, message=message)

        return render_template('project-6.html', current_year=current_year, msg_sent=True, form=form)

    return render_template('project-6.html', current_year=current_year, msg_sent=False, form=form)

    return render_template('project-6.html', current_year=current_year, msg_sent=False)


@app.route('/download', methods=['GET', 'POST'])
def download():
    return send_from_directory('static', path="files/CV.pdf", as_attachment=True)


# TODO Add url to Go back to portfolio button
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
