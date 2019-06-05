from datetime import datetime
from app import db


class Client(db.Model):

    id = db.Column(db.Integer, primary_key=True, index=True, unique=True)
    fio = db.Column(db.String(30))
    phone = db.Column(db.String(30), unique=True)
    address = db.Column(db.String(30))
    DOB = db.Column(db.Date, index=True)
    receptions = db.relationship('Reception', backref = 'reception_client', lazy = 'dynamic')

class Doctor(db.Model):

    id = db.Column(db.Integer, primary_key=True, index=True, unique=True)
    fio = db.Column(db.String(30))
    phone = db.Column(db.String(30))
    specialty_id = db.Column(db.Integer, db.ForeignKey('specialty.id'))
    employmentDate = db.Column(db.Date, index=True)
    receptions = db.relationship('Reception', backref = 'reception_doctor', lazy = 'dynamic')

class Service(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(30), index=True, unique=True)
    price = db.Column(db.Integer, index=True)
    type_id = db.Column(db.Integer, db.ForeignKey('type.id'))
    receptions = db.relationship('Reception', backref = 'reception_service', lazy = 'dynamic')

class Type(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    category = db.Column(db.String(30), index=True, unique=True)
    services = db.relationship('Service', backref = 'service_type', lazy = 'dynamic')

class Reception(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    client_id = db.Column(db.Integer, db.ForeignKey('client.id'))
    doctor_id = db.Column(db.Integer, db.ForeignKey('doctor.id'))
    service_id = db.Column(db.Integer, db.ForeignKey('service.id'))
    date = db.Column(db.Date, index=True)
    count = db.Column(db.Integer)

class Specialty(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(30), index=True, unique=True)
    doctors = db.relationship('Doctor', backref = 'doctor_specialty', lazy = 'dynamic')