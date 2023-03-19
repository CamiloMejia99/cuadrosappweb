from . import paginacion
from flask import Flask, render_template, request, redirect, url_for
from conexionBD import *  #Importando conexion BD
from funciones import *  #Importando mis Funciones
from flask import Flask, render_template, request, url_for
import mysql.connector

from babel import numbers, dates
from datetime import date, datetime, time
from flask_babel import Babel, gettext, refresh; refresh()

app = Flask(__name__)


config = {
  'host': 'localhost',
  'user': 'root',
  'passwd': '',
  'database': 'cuadros_c',
}

app.config ['BABEL_DEFAULT_LOCALE'] = 'en'
babel = Babel(app)

def get_locale():
    return request.accept_languages.best_match('en', 'es', 'fr ')
babel = Babel(app, locale_selector=get_locale)

Listado_usuarios = gettext('Listado de usuarios')
INFORMACION_USUARIOS = gettext('INFORMACION USUARIOS')
Nombre = gettext('Nombre')
INFORMACION_PQRS = gettext('INFORMACION PQRS')
Listado_opiniones = gettext('Listado de opiniones')
Apellido = gettext('Apellido')
Correo = gettext('Correo')
Sugerencia = gettext('Sugerencia')


@paginacion.route('/paginacion')
def precios():
     conn = mysql.connector.connect(**config)
     cursor = conn.cursor()
     cursor.execute("SELECT * FROM users LIMIT 0,4")
     users = cursor.fetchall()
     cursor.execute("SELECT * FROM pqrs LIMIT 0,4")
     pqrs = cursor.fetchall()
     conn.commit()
     return render_template('paginacion.html',dataLogin = dataLoginSesion(), users=users, pqrs=pqrs)


@paginacion.route("/page/<number_page>")
def page(number_page):
  conn = mysql.connector.connect(**config)
  cursor = conn.cursor()

  #listado de usuarios

  if number_page == '1':
    cursor.execute("SELECT * FROM users LIMIT 0,4")
  if number_page == '2':
    cursor.execute("SELECT * FROM users LIMIT 4,4")
  if number_page == '3':
    cursor.execute("SELECT * FROM users LIMIT 8,4")
  if number_page == '4':
    cursor.execute("SELECT * FROM users LIMIT 12,4")
 
  users = cursor.fetchall()
  list_users = len(users)
  conn.commit()
  
  #listado de quejas
    
  if number_page == '1':
    cursor.execute("SELECT * FROM pqrs LIMIT 0,4")
  if number_page == '2':
    cursor.execute("SELECT * FROM pqrs LIMIT 4,4")
  if number_page == '3':
    cursor.execute("SELECT * FROM pqrs LIMIT 8,4")
  if number_page == '4':
    cursor.execute("SELECT * FROM pqrs LIMIT 12,4")
 
  pqrs = cursor.fetchall()
  list_pqrs = len(pqrs)
  
  conn.commit()
  return render_template('paginacion.html', users=users, pqrs=pqrs)


