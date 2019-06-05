from flask import abort, flash, redirect, render_template, url_for
from flask_login import current_user, login_required
from . import admin
from .forms import ClientForm, TypeForm, DoctorForm, SpecialtyForm, ServiceForm, ReceptionForm
from .. import db
from ..models import Client, Type, Doctor, Specialty, Service, Reception


@admin.route('/types')
def list_types():
    types = Type.query.all()
    return render_template('admin/types/types.html',
                           types=types, title='Types')

@admin.route('/types/add', methods=['GET', 'POST'])
def add_type():
    add_type = True
    form = TypeForm()
    if form.validate_on_submit():
        type = Type(category=form.category.data)
        try:
            db.session.add(type)
            db.session.commit()
            flash('You have successfully added a new type.')
        except:
            flash('Error: type name already exists.')
        return redirect(url_for('admin.list_types'))
    return render_template('admin/types/type.html', add_type=add_type,
                           form=form, title='Add Type')

@admin.route('/types/edit/<int:id>', methods=['GET', 'POST'])
def edit_type(id):
    add_type = False
    type = Type.query.get_or_404(id)
    form = TypeForm(obj=type)
    if form.validate_on_submit():
        type.category = form.category.data
        db.session.add(type)
        db.session.commit()
        flash('You have successfully edited the type.')
        return redirect(url_for('admin.list_types'))

    form.category.data = type.category
    return render_template('admin/types/type.html', add_type=add_type,
                           form=form, title="Edit Type")

@admin.route('/types/delete/<int:id>', methods=['GET', 'POST'])
def delete_type(id):
    type = Type.query.get_or_404(id)
    if not type.services.all():
        db.session.delete(type)
        db.session.commit()
        flash('You have successfully deleted the type.')
    else:
        flash('Delete related services.')
    return redirect(url_for('admin.list_types'))

@admin.route('/clients')
def list_clients():
    clients = Client.query.all()
    return render_template('admin/clients/clients.html',
                           clients=clients, title='Clients')

@admin.route('/clients/add', methods=['GET', 'POST'])
def add_client():
    add_client = True
    form = ClientForm()
    if form.validate_on_submit():
        client = Client(fio=form.fio.data,
                      phone=form.phone.data,
                      address=form.address.data,
                      DOB=form.DOB.data
                      )
        try:
            db.session.add(client)
            db.session.commit()
            flash('You have successfully added a new client.')
        except:
            flash('Error: client name already exists.')
        return redirect(url_for('admin.list_clients'))
    return render_template('admin/clients/client.html', add_client=add_client,
                           form=form, title='Add Client')

@admin.route('/clients/edit/<int:id>', methods=['GET', 'POST'])
def edit_client(id):
    add_client = False
    client = Client.query.get_or_404(id)
    form = ClientForm(obj=client)
    if form.validate_on_submit():
        client.fio = form.fio.data
        client.phone = form.phone.data
        client.address = form.address.data
        client.DOB = form.DOB.data
        db.session.add(client)
        db.session.commit()
        flash('You have successfully edited the point.')
        return redirect(url_for('admin.list_clients'))
    form.fio.data = client.fio
    form.phone.data = client.phone
    form.address.data = client.address
    form.DOB.data = client.DOB
    return render_template('admin/clients/client.html', add_client=add_client,
                           form=form, title="Edit Client")

@admin.route('/clients/delete/<int:id>', methods=['GET', 'POST'])
def delete_client(id):
    client = Client.query.get_or_404(id)
    if not client.receptions.all():
        db.session.delete(client)
        db.session.commit()
        flash('You have successfully deleted the client.')
    else:
        flash('Delete related receptions.')
    return redirect(url_for('admin.list_clients'))


@admin.route('/doctors')
def list_doctors():
    doctors = Doctor.query.all()
    specialtys = {specialty.id: specialty.title for specialty in Specialty.query.all()}
    return render_template('admin/doctors/doctors.html',
                           doctors=doctors,
                           specialtys=specialtys,
                            title='Doctors')

@admin.route('/doctors/add', methods=['GET', 'POST'])
def add_doctor():
    add_doctor = True
    form = DoctorForm()
    if form.validate_on_submit():
        doctor = Doctor(fio=form.fio.data,
                      phone=form.phone.data,
                      specialty_id=form.specialty_id.data.id,
                      employmentDate=form.employmentDate.data
                      )
        try:
            db.session.add(doctor)
            db.session.commit()
            flash('You have successfully added a new doctor.')
        except:
            flash('Error: doctor name already exists.')
        return redirect(url_for('admin.list_doctors'))
    return render_template('admin/doctors/doctor.html', add_doctor=add_doctor,
                           form=form, title='Add Doctor')

@admin.route('/doctors/edit/<int:id>', methods=['GET', 'POST'])
def edit_doctor(id):
    add_doctor = False
    doctor = Doctor.query.get_or_404(id)
    form = DoctorForm(obj=doctor)
    if form.validate_on_submit():
        doctor.fio = form.fio.data
        doctor.phone = form.phone.data
        doctor.specialty_id = form.specialty_id.data.id
        doctor.employmentDate = form.employmentDate.data
        db.session.add(doctor)
        db.session.commit()
        flash('You have successfully edited the point.')
        return redirect(url_for('admin.list_doctors'))
    form.fio.data = doctor.fio
    form.phone.data = doctor.phone
    form.specialty_id.data =doctor.specialty_id
    form.employmentDate.data = doctor.employmentDate
    return render_template('admin/doctors/doctor.html', add_doctor=add_doctor,
                           form=form, title="Edit Doctor")

@admin.route('/doctors/delete/<int:id>', methods=['GET', 'POST'])
def delete_doctor(id):
    doctor = Doctor.query.get_or_404(id)
    if not doctor.receptions.all():
        db.session.delete(doctor)
        db.session.commit()
        flash('You have successfully deleted the doctor.')
    else:
        flash('Delete related receptions.')
    return redirect(url_for('admin.list_doctors'))
 
@admin.route('/specialtys')
def list_specialtys():
    specialtys = Specialty.query.all()
    return render_template('admin/specialtys/specialtys.html',
                           specialtys=specialtys, title='specialtys')

@admin.route('/specialtys/add', methods=['GET', 'POST'])
def add_specialty():
    add_specialty = True
    form = SpecialtyForm()
    if form.validate_on_submit():
        specialty = Specialty(title=form.title.data)
        try:
            db.session.add(specialty)
            db.session.commit()
            flash('You have successfully added a new specialty.')
        except:
            flash('Error: specialty name already exists.')
        return redirect(url_for('admin.list_specialtys'))
    return render_template('admin/specialtys/specialty.html', add_specialty=add_specialty,
                           form=form, title='Add Specialty')

@admin.route('/specialtys/edit/<int:id>', methods=['GET', 'POST'])
def edit_specialty(id):
    add_specialty = False
    specialty = Specialty.query.get_or_404(id)
    form = SpecialtyForm(obj=specialty)
    if form.validate_on_submit():
        specialty.title = form.title.data
        db.session.add(specialty)
        db.session.commit()
        flash('You have successfully edited the specialty.')
        return redirect(url_for('admin.list_specialtys'))

    form.title.data = specialty.title
    return render_template('admin/specialtys/specialty.html', add_specialty=add_specialty,
                           form=form, title="Edit Specialty")

@admin.route('/specialtys/delete/<int:id>', methods=['GET', 'POST'])
def delete_specialty(id):
    specialty = Specialty.query.get_or_404(id)
    if not specialty.doctors.all():
        db.session.delete(specialty)
        db.session.commit()
        flash('You have successfully deleted the specialty.')
    else:
        flash('Delete related doctors.')
    return redirect(url_for('admin.list_specialtys'))

@admin.route('/services')
def list_services():
    services = Service.query.all()
    types = {type.id: type.category for type in Type.query.all()}
    return render_template('admin/services/services.html',
                           services=services,
                           types=types,
                           title='Services')

@admin.route('/services/add', methods=['GET', 'POST'])
def add_service():
    add_service = True
    form = ServiceForm()
    if form.validate_on_submit():
        service = Service(title=form.title.data,
                          type_id=form.type_id.data.id,
                          price=form.price.data)
        try:
            db.session.add(service)
            db.session.commit()
            flash('You have successfully added a new service.')
        except:
            flash('Error: service title already exists.')
        return redirect(url_for('admin.list_services'))
    return render_template('admin/services/service.html', add_service=add_service,
                           form=form, title='Add Service')

@admin.route('/services/edit/<int:id>', methods=['GET', 'POST'])
def edit_service(id):
    add_service = False
    service = Service.query.get_or_404(id)
    form = ServiceForm(obj=service)
    if form.validate_on_submit():
        service.title = form.title.data
        service.type_id = form.type_id.data.id
        service.price = form.price.data
        db.session.add(service)
        db.session.commit()
        flash('You have successfully edited the service.')
        return redirect(url_for('admin.list_services'))
    form.title.data = service.title
    form.type_id.data = service.type_id
    form.price.data = service.price
    return render_template('admin/services/service.html', add_service=add_service,
                           form=form, title="Edit Service")

@admin.route('/services/delete/<int:id>', methods=['GET', 'POST'])
def delete_service(id):
    service = Service.query.get_or_404(id)
    if not service.receptions.all():
        db.session.delete(service)
        db.session.commit()
        flash('You have successfully deleted the service.')
    else:
        flash('Delete related reception.')   
    return redirect(url_for('admin.list_services'))

@admin.route('/receptions')
def list_receptions():
    receptions = Reception.query.all()
    clients = {client.id: client.fio for client in Client.query.all()}
    doctors = {doctor.id: doctor.fio for doctor in Doctor.query.all()}
    services = {service.id: service.title for service in Service.query.all()}
    counts = {service.id: service.price for service in Service.query.all()}
    return render_template('admin/receptions/receptions.html',
                           receptions=receptions,
                           clients=clients,
                           doctors=doctors,
                           services=services,
                           counts=counts,
                           title='receptions')

@admin.route('/receptions/add', methods=['GET', 'POST'])
def add_reception():
    add_reception = True
    form = ReceptionForm()
    if form.validate_on_submit():
        reception = Reception(client_id=form.client_id.data.id,
                      doctor_id=form.doctor_id.data.id,
                      service_id=form.service_id.data.id,
                      date=form.date.data,
                      count=form.service_id.data.price)
        try:
            db.session.add(reception)
            db.session.commit()
            flash('You have successfully added a new reception.')
        except:
            flash('Error: reception name already exists.')
        return redirect(url_for('admin.list_receptions'))
    return render_template('admin/receptions/reception.html', add_reception=add_reception,
                           form=form, title='Add Reception')

@admin.route('/receptions/edit/<int:id>', methods=['GET', 'POST'])
def edit_reception(id):
    add_reception = False
    reception = Reception.query.get_or_404(id)
    form = ReceptionForm(obj=reception)
    if form.validate_on_submit():
        reception.client_id=form.client_id.data.id
        reception.doctor_id=form.doctor_id.data.id
        reception.service_id=form.service_id.data.id
        reception.date=form.date.data
        reception.count=form.service_id.data.price
        db.session.add(reception)
        db.session.commit()
        flash('You have successfully edited the reception.')
        return redirect(url_for('admin.list_receptions'))
    form.client_id.data = reception.client_id
    form.doctor_id.data = reception.doctor_id
    form.service_id.data = reception.service_id
    form.date.data = reception.date
    form.count.data = reception.count
    return render_template('admin/receptions/reception.html', add_reception=add_reception,
                           form=form, title="Edit Reception")

@admin.route('/receptions/delete/<int:id>', methods=['GET', 'POST'])
def delete_reception(id):
    reception = Reception.query.get_or_404(id)
    db.session.delete(reception)
    db.session.commit()
    flash('You have successfully deleted the reception.')
 
    return redirect(url_for('admin.list_receptions'))
