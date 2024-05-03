from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField
from wtforms.validators import DataRequired, URL, Email, Length, ValidationError, InputRequired

class ContactForm(FlaskForm):
    name = StringField(label='Name', validators=[DataRequired(), Length(max=64)],
                                render_kw={"placeholder": "Name", "class": "contact-form"})

    email = StringField(label='Email', validators=[DataRequired(), Email(message="You seem to be missing @ or .", check_deliverability=True)],
                        render_kw={"placeholder": "Email", "class": "col-6 col-12-medium"})

    subject= StringField(label='Subject', validators=[DataRequired(), Length(max=64)],
                                render_kw={"placeholder": "Subject", "class": "col-12"})

    message = TextAreaField(label='Message', validators=[DataRequired()],
                                     render_kw={"placeholder": "Enter your message here",  "class": "col-12"})

    submit = SubmitField(label='Send Message', render_kw={"class": "btn btn-dark col-12", "id":"contact_submit_btn" })
