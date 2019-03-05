#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pymysql
DB_HOST     = ''
DB_USER     = ''
DB_PASSWORD = ''
DB_DBNAME   = ''
conn = pymysql.connect(host=DB_HOST, user=DB_USER, password=DB_PASSWORD, db=DB_DBNAME, cursorclass=pymysql.cursors.DictCursor)
cur = conn.cursor()


def agregar_contacto(name, lastName, address, city, phone, email):
    '''
    Agrega un contacto a la base de datos
    '''
    # TODO: almacene en la variable query la sentencia sql
    #       para agregar el contacto con los datos suministrados
    query = ''
    cur.execute(query)


def obtener_contactos():
    '''
    Devuelve la lista completa de contactos
    '''
    # TODO: almacene en la variable query la sentencia sql para
    #       obtener todos los contactos
    query = ''
    
    try:
        cur.execute(query)
        contactos = []
        for c in cur.fetchall():
            contactos.append(
                {
                    'id': c['id'],
                    'name': c['name'],
                    'lastName': c['lastName'],
                    'address': c['address'],
                    'city': c['city'],
                    'phone': c['phone'],
                    'email': c['email'],
                }
            )
        return contactos
    except pymysql.err.InternalError as e:
        if e.args[1] == 'Query was empty':
            return []
        else:
            raise e
    
    


def filtrar_contactos(filtro=''):
    '''
    Devuelve la lista de contactos cuyo nombre
    o apellido coincida con el término filtro
    '''
    # TODO: almacene en la variable query la sentencia sql para
    #       obtener los contactos de acuerdo al criterio de filtrado
    query = ''
    try:
        cur.execute(query)
        contactos = []
        for c in cur.fetchall():
            contactos.append(
                {
                    'id': c['id'],
                    'name': c['name'],
                    'lastName': c['lastName'],
                    'address': c['address'],
                    'city': c['city'],
                    'phone': c['phone'],
                    'email': c['email'],
                }
            )
        return contactos
    except pymysql.err.InternalError as e:
        if e.args[1] == 'Query was empty':
            return []
        else:
            raise e


def eliminar_contacto(id_contacto):
    '''
    Elimina un contacto de la base de datos a partir de su id
    '''
    # TODO: almacene en la variable query la sentencia sql para
    # eliminar el contacto con id: id_contacto
    query = ''
    cur.execute(query)
    

def obtener_contacto(id_contacto):
    '''
    Devuelve los datos de un contacto de la lista a partir de su id
    '''
    # TODO: almacene en la variable query la sentencia sql para
    # obtener los datos del contacto con id: id_contacto
    query = ''
    cur.execute(query)
    c = cur.fetchall()[0]
    contacto = {
        'name': c['name'],
        'lastName': c['lastName'],
        'address': c['address'],
        'city': c['city'],
        'phone': c['phone'],
        'email': c['email'],
    }
    return contactos


def editar_contacto(id_contacto, name, lastName, address, city, phone, email):
    '''
    Modifica la información del contacto con el id_contacto especificado
    '''
    # TODO: almacene en la variable query la sentencia sql para
    # modificar el contacto con id: id_contacto de acuerdo a los datos suministrados
    query = ''
    cur.execute(query)