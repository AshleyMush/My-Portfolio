from flask import Flask, abort, render_template, redirect, url_for, flash, request, send_from_directory
from flask_bootstrap import Bootstrap5
from datetime import datetime
from flask_ckeditor import CKEditor
import smtplib
import os







app = Flask(__name__)
app.config['SECRET_KEY'] = os.environ.get("SECRET_APP_KEY")
ckeditor = CKEditor(app)
Bootstrap5(app)


@app.route('/', methods =['GET', 'POST'])
def home():
    current_year = datetime.now().year


    return render_template('index.html', current_year=current_year)


@app.route('/project-1', methods = ['GET', 'POST'])
def project1():
    return render_template('project-1.html')


@app.route('/project-2', methods = ['GET', 'POST'])
def project2():
    return render_template('project-2.html')

@app.route('/project-3', methods = ['GET', 'POST'])
def project3():
    return render_template('project-3.html')

@app.route('/project-4', methods = ['GET', 'POST'])
def project4():
    return render_template('project-4.html')

@app.route('/project-5', methods = ['GET', 'POST'])
def project5():
    return render_template('project-5.html')


@app.route('/project-6', methods = ['GET', 'POST'])
def project6():
    return render_template('project-6.html')

@app.route('/download', methods=['GET','POST'])
def download():
    return send_from_directory('static', path="files/cheat_sheet.pf")









if __name__ == "__main__":
    app.run(debug=True, port=5002)