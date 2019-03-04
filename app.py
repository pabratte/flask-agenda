#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask import Flask, url_for, render_template, request, redirect
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
from flask_wtf import FlaskForm
import agenda

app = Flask(__name__)
app.config['SECRET_KEY'] = 'you-will-never-guess'

class ContactForm(FlaskForm):
    name        = StringField('Nombre', validators=[DataRequired()])
    lastName    = StringField('Apellido', validators=[DataRequired()])
    address     = StringField('Direccion', validators=[DataRequired()])
    city        = StringField('Ciudad', validators=[DataRequired()])
    phone       = StringField('Telefono', validators=[DataRequired()])
    email       = StringField('Email', validators=[DataRequired()])

class ContactEditForm(FlaskForm):
    name        = StringField('Nombre', validators=[DataRequired()])
    lastName    = StringField('Apellido', validators=[DataRequired()])
    address     = StringField('Direccion', validators=[DataRequired()])
    city        = StringField('Ciudad', validators=[DataRequired()])
    phone       = StringField('Telefono', validators=[DataRequired()])
    email       = StringField('Email', validators=[DataRequired()])

@app.route('/')
def index():
    return render_template('list.html', contacts=agenda.obtener_contactos())


@app.route('/add', methods=['GET', 'POST'])
def add():
    form = ContactForm(request.form)
    if request.method == 'POST' and form.validate():
        newContact = {
            'name': form.name.data,
            'lastName': form.lastName.data,
            'address': form.address.data,
            'city': form.city.data,
            'phone': form.phone.data,
            'email': form.email.data,
        }
        print newContact
        agenda.agregar(newContact)
        return redirect(url_for('index'))
    return render_template('add.html', form=form)


@app.route('/edit/<int:id_contact>', methods=['GET', 'POST'])
def edit(id_contact):
    contact = agenda.obtener_contacto(id_contact)
    form = ContactEditForm(data=contact)
    if request.method == 'POST' and form.validate():
        contactoEditado = {
            'name': form.name.data,
            'lastName': form.lastName.data,
            'address': form.address.data,
            'city': form.city.data,
            'phone': form.phone.data,
            'email': form.email.data,
        }
        agenda.editar_contacto(contactoEditado)
    return render_template('add.html', form=form)