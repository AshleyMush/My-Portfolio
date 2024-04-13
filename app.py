from flask import Flask, abort, render_template, redirect, url_for, flash, request
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
    return render_template('project-2.html')









if __name__ == "__main__":
    app.run(debug=True, port=5002)