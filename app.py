#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask import Flask, url_for, render_template, request, redirect
import agenda

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('list.html', contacts=agenda.obtener_contactos())

@app.route('/add', methods=['GET', 'POST'])
def add():
    if request.method == 'POST':
        
        newContact = {
            'name': request.form.get('name'),
            'lastName': request.form.get('lastName'),
            'address': request.form.get('address'),
            'city': request.form.get('city'),
            'phone': request.form.get('phone'),
            'email': request.form.get('email'),
        }
        print newContact
        agenda.agregar(newContact)
        return redirect(url_for('index'))
    return render_template('add.html')

