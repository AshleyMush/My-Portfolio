from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField
from wtforms.validators import DataRequired, URL, Email, Length, ValidationError, InputRequired


class ContactForm(FlaskForm):
    name = StringField(label='Name', validators=[DataRequired(), Length(max=64)],
                                render_kw={"placeholder": "Name", "class": "contact-form"})
    #Name:

    email = StringField(label='Email', validators=[DataRequired(), Email(message="You seem to be missing @ or .", check_deliverability=True)],
                        render_kw={"placeholder": "Email", "class": "contact-form"})

    subject= StringField(label='Subject', validators=[DataRequired(), Length(max=64)],
                                render_kw={"placeholder": "Subject", "class": "contact-form"})

    message = TextAreaField('Message', validators=[DataRequired()],
                                     render_kw={"placeholder": "Reason for call back",  "class": "contact-form"})

    submit = SubmitField(label='Send Message', render_kw={"class": "btn btn-dark", "id":"contact_submit_btn" })
