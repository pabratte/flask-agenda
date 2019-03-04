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
        'id': 2,
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
def agregar_contacto(nuevo_contacto):
    nuevo_contacto['id'] = len(contactos)+1
    contactos.append(nuevo_contacto)


def obtener_contactos(filtro=''):
    filtro = filtro.lower()
    if filtro == '':
        return contactos
    else:
        contactos_filtrados = []
        for c in contactos:
            if c['name'].lower().find(filtro) != -1 or c['lastName'].lower().find(filtro) != -1:
                contactos_filtrados.append(c) 
        return contactos_filtrados


def eliminar_contacto(id_contacto):
    for i in range(0, len(contactos)):
        if contactos[i]['id'] == int(id_contacto):
            print "Eliminando...."
            contactos.pop(i)
            return
    

def obtener_contacto(id_contacto):
    for c in contactos:
        if c['id'] == id_contacto:
            return c
    return None


def editar_contacto(id_contacto, info_contacto):
    for c in contactos:
        if c['id'] == int(id_contacto):
            c['name'] = info_contacto['name']
            c['lastName'] = info_contacto['lastName']
            c['address'] = info_contacto['address']
            c['city'] = info_contacto['city']
            c['phone'] = info_contacto['phone']
            c['email'] = info_contacto['email']
            return