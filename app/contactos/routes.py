from . import contacto
from flask import render_template
from flask import Flask, session, render_template, request, redirect, url_for
from conexionBD import *  #Importando conexion BD
from funciones import *  #Importando mis Funciones

from babel import numbers, dates
from datetime import date, datetime, time
from flask_babel import Babel, gettext, refresh; refresh()

app = Flask(__name__)

@contacto.route('/contactos')
def contactos():
     return render_template('contactos.html',dataLogin = dataLoginSesion())

app.config ['BABEL_DEFAULT_LOCALE'] = 'en'
babel = Babel(app)

def get_locale():
    return request.accept_languages.best_match('en', 'es', 'fr ')
babel = Babel(app, locale_selector=get_locale)


SUSCRIBETE = gettext('SUSCRIBETE')
Se_primero_recibir_información_nuestras_promociones = gettext('Sé el primero en recibir información de nuestras promociones')
Enviar = gettext('Enviar')
Siguenos_nuestras_redes_sociales = gettext('Siguenos en nuestras redes sociales')
