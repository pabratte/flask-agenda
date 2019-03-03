#!/usr/bin/env python
# -*- coding: utf-8 -*-

contactos = [
    {
        'id': 1,
        'name': 'Rick',
        'lastName': 'Sanchez',
        'address': '?',
        'city': 'Washington',
        'phone': '012589642565',
        'email': 'rsanchez@gmail.com'
    },
    {
        'id': 1,
        'name': 'Homero',
        'lastName': 'Simpson',
        'address': 'Av. Siempreviva 123',
        'city': 'Washington',
        'phone': '012589642565',
        'email': 'rsanchez@gmail.com'
    }
]

'''
Recibe un objeto con la forma:
nuevoContacto = {
    'name': 'Rick',
    'lastName': 'Sanchez',
    'address': '?',
    'city': 'Washington',
    'phone': '012589642565',
    'email': 'rsanchez@gmail.com'
},
'''
def agregar(nuevo_contacto):
    nuevo_contacto['id'] = len(contactos)+1
    contactos.append(nuevo_contacto)


def obtener_contactos():
    return contactos


def eliminar_contactos(id_contactos):
    pass    