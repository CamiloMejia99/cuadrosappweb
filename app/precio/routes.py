from . import precio
from flask import render_template
from conexionBD import *  #Importando conexion BD
from funciones import *  #Importando mis Funciones
@precio.route('/precio')
def precios():
     return render_template('precio.html',dataLogin = dataLoginSesion())