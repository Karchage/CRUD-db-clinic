from flask_wtf import FlaskForm
from wtforms import DateField, IntegerField, StringField, SubmitField, HiddenField, Label
from wtforms.ext.sqlalchemy.fields import QuerySelectField
from wtforms.validators import DataRequired, Optional

from ..models import Client, Doctor, Service, Type, Specialty, Reception

class ClientForm(FlaskForm):
    fio = StringField('Fio', validators=[DataRequired()])
    phone = StringField('Phone', validators=[DataRequired()])
    address = StringField('Address', validators=[DataRequired()])
    DOB = DateField('DOB', validators=[DataRequired()])
    submit = SubmitField('Submit')

class DoctorForm(FlaskForm):
    fio = StringField('Fio', validators=[DataRequired()])
    phone = StringField('Phone', validators=[DataRequired()])
    specialty_id = QuerySelectField(query_factory=lambda: Specialty.query.all(), get_label="title")
    employmentDate = DateField('employmentDate', validators=[DataRequired()])
    submit = SubmitField('Submit')

class TypeForm(FlaskForm):
    category = StringField('Category', validators=[DataRequired()])
    submit = SubmitField('Submit')

class SpecialtyForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired()])
    submit = SubmitField('Submit')

class ServiceForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired()])
    price = IntegerField('Price', validators=[DataRequired()])
    type_id = QuerySelectField(query_factory=lambda: Type.query.all(), get_label="category")
    submit = SubmitField('Submit')

class ReceptionForm(FlaskForm):
    client_id = QuerySelectField(query_factory=lambda: Client.query.all(), get_label="fio")
    doctor_id = QuerySelectField(query_factory=lambda: Doctor.query.all(), get_label="fio")
    service_id = QuerySelectField(query_factory=lambda: Service.query.all(), get_label="title")
    date = DateField('Date', validators=[DataRequired()])
    count = HiddenField('Price', validators=[Optional()])
    submit = SubmitField('Submit')