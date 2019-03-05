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


def agregar_contacto(name, lastName, address, city, phone, email):
    '''
    Agrega un contacto a la lista
    '''
    contactos.append(
        {
            'id': len(contactos)+1,
            'name': name,
            'lastName': lastName,
            'address': address,
            'city': city,
            'phone': phone,
            'email': email
        }
    )


def obtener_contactos():
    '''
    Devuelve la lista completa de contactos
    '''
    return contactos


def filtrar_contactos(filtro=''):
    '''
    Devuelve la lista de contactos cuyo nombre
    o apellido coincida con el término filtro
    '''
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
    '''
    Elimina un contacto de la lista a partir de su id
    '''
    for i in range(0, len(contactos)):
        if contactos[i]['id'] == int(id_contacto):
            contactos.pop(i)
            return
    

def obtener_contacto(id_contacto):
    '''
    Devuelve un diccionario con los datos de un
    contacto de la lista a partir de su id
    '''
    for c in contactos:
        if c['id'] == id_contacto:
            return c
    return None


def editar_contacto(id_contacto, name, lastName, address, city, phone, email):
    '''
    Modifica la información del contacto con el id_contacto especificado
    '''
    for c in contactos:
        if c['id'] == int(id_contacto):
            c['name'] = name
            c['lastName'] = lastName
            c['address'] = address
            c['city'] = city
            c['phone'] = phone
            c['email'] = email
            return