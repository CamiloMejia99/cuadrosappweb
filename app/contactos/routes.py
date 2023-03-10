from . import contacto
from flask import render_template
from conexionBD import *  #Importando conexion BD
from funciones import *  #Importando mis Funciones
@contacto.route('/contactos')
def contactos():
     return render_template('contactos.html',dataLogin = dataLoginSesion())