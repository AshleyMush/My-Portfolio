This project is a portfolio website developed using Flask, a Python web framework. The website showcases various projects and includes a contact form for visitors to send messages. The website also includes a login form for user authentication.

📉Technologies Used
Python
Flask
Flask-WTF for form handling
Flask-Bootstrap for Bootstrap integration
Flask-SQLAlchemy for database handling
SQLite for the database
HTML/CSS/JavaScript for frontend
Bootstrap for styling

🔥Features
Display of various projects
Contact form for visitors to send messages
Login form for user authentication
Downloadable CV

👇Installation
To install the project, clone the repository and install the required packages using pip:
![image](https://github.com/AshleyMush/My-Portfolio/assets/49234738/2b4f4b35-8260-4218-b4d1-a1bae42ba048)
git clone <repository-url>
cd <repository-directory>
pip install -r requirements.txt

Usage
To run the project, use the following command:
python app.py

⛔TODOs
Template Rendering and Database Integration: 
![image](https://github.com/AshleyMush/My-Portfolio/assets/49234738/4456f7e7-8296-4a07-8b9f-ed78d4a30c6d)


The current project structure uses static HTML files for each project. The goal is to transition to dynamic template rendering using Flask's Jinja2 template engine. The project data will be stored in a SQLite database (Portfolio.db), and Flask-SQLAlchemy will be used to fetch and display this data on the website. 




User Authentication: The website currently includes a basic login form. The goal is to add backend functionality for user authentication. This will involve handling the form submission, verifying the user credentials, and managing user sessions.  
Form Styling: The forms on the website are currently rendered using Flask-Bootstrap's render_form function. The goal is to transition to manual form rendering, which will provide more control over the form layout and styling. Bootstrap will be used to style the forms. 



