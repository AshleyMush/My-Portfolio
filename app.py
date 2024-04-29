from flask import Flask, abort, render_template, redirect, url_for, flash, request, send_from_directory
from flask_bootstrap import Bootstrap5
from datetime import datetime
from flask_ckeditor import CKEditor
import smtplib
from email.mime.text import MIMEText
import smtplib
import os

MY_EMAIL_ADDRESS = os.environ.get("EMAIL_KEY")
MY_EMAIL_APP_PASSWORD = os.environ.get("PASSWORD_KEY")

app = Flask(__name__)
app.config['SECRET_KEY'] = os.environ.get("SECRET_APP_KEY")
ckeditor = CKEditor(app)
Bootstrap5(app)


#TODO Add Favicon

@app.route('/', methods=['GET', 'POST'])
def home():
    current_year = datetime.now().year

    if request.method == "POST":
        data = request.form

        name, email, subject, message = data['name'], data['email'], data['subject'], data['message']

        print(f"{name, email, subject, message}")

        send_confirmation_email(name=name, email=email, subject=subject)
        send_email(name=name, subject=subject, email=email, message=message)
        return render_template('index.html', current_year=current_year, msg_sent=True)

    return render_template('index.html', current_year=current_year, msg_sent=False)



# @app.route('/example', methods=['GET', 'POST'])
# def example():
#     current_year = datetime.now().year
#
#     if request.method == "POST":
#         data = request.form
#
#         name, email, subject, message = data['name'], data['email'], data['subject'], data['message']
#
#         print(f"{name, email, subject, message}")
#
#         send_confirmation_email(name=name, email=email, subject=subject)
#         send_email(name=name, subject=subject, email=email, message=message)
#         return render_template('project-1.html', current_year=current_year, msg_sent=True)
#
#     return render_template('example-template.html', current_year=current_year, msg_sent=False)



@app.route('/project-1', methods=['GET', 'POST'])
def project1():
    current_year = datetime.now().year

    if request.method == "POST":
        data = request.form

        name, email, subject, message = data['name'], data['email'], data['subject'], data['message']

        print(f"{name, email, subject, message}")

        send_confirmation_email(name=name, email=email, subject=subject)
        send_email(name=name, subject=subject, email=email, message=message)
        return render_template('project-1.html', current_year=current_year, msg_sent=True)

    return render_template('project-1.html', current_year=current_year, msg_sent=False)


@app.route('/project-2', methods=['GET', 'POST'])
def project2():
    current_year = datetime.now().year

    if request.method == "POST":
        data = request.form

        name, email, subject, message = data['name'], data['email'], data['subject'], data['message']

        print(f"{name, email, subject, message}")

        send_confirmation_email(name=name, email=email, subject=subject)
        send_email(name=name, subject=subject, email=email, message=message)
        return render_template('project-2.html', current_year=current_year, msg_sent=True)

    return render_template('project-2.html', current_year=current_year, msg_sent=False)


@app.route('/project-3', methods=['GET', 'POST'])
def project3():
    current_year = datetime.now().year

    if request.method == "POST":
        data = request.form

        name, email, subject, message = data['name'], data['email'], data['subject'], data['message']

        print(f"{name, email, subject, message}")

        send_confirmation_email(name=name, email=email, subject=subject)
        send_email(name=name, subject=subject, email=email, message=message)
        return render_template('project-3.html', current_year=current_year, msg_sent=True)

    return render_template('project-3.html', current_year=current_year, msg_sent=False)


@app.route('/project-4', methods=['GET', 'POST'])
def project4():
    current_year = datetime.now().year

    if request.method == "POST":
        data = request.form

        name, email, subject, message = data['name'], data['email'], data['subject'], data['message']

        print(f"{name, email, subject, message}")

        send_confirmation_email(name=name, email=email, subject=subject)
        send_email(name=name, subject=subject, email=email, message=message)
        return render_template('project-4.html', current_year=current_year, msg_sent=True)

    return render_template('project-4.html', current_year=current_year, msg_sent=False)


@app.route('/project-5', methods=['GET', 'POST'])
def project5():
    current_year = datetime.now().year

    if request.method == "POST":
        data = request.form

        name, email, subject, message = data['name'], data['email'], data['subject'], data['message']

        print(f"{name, email, subject, message}")

        send_confirmation_email(name=name, email=email, subject=subject)
        send_email(name=name, subject=subject, email=email, message=message)
        return render_template('project-5.html', current_year=current_year, msg_sent=True)

    return render_template('project-5.html', current_year=current_year, msg_sent=False)


@app.route('/project-6', methods=['GET', 'POST'])
def project6():
    current_year = datetime.now().year

    if request.method == "POST":
        data = request.form

        name, email, subject, message = data['name'], data['email'], data['subject'], data['message']

        print(f"{name, email, subject, message}")

        send_confirmation_email(name=name, email=email, subject=subject)
        send_email(name=name, subject=subject, email=email, message=message)
        return render_template('project-6.html', current_year=current_year, msg_sent=True)

    return render_template('project-6.html', current_year=current_year, msg_sent=False)


@app.route('/download', methods=['GET', 'POST'])
def download():
    return send_from_directory('static', path="files/CV.pdf", as_attachment=True)





#TODO Add url to Go back to portfolio button
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
