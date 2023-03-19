from . import tipo
from flask import render_template
from conexionBD import *  #Importando conexion BD
from funciones import *  #Importando mis Funciones
@tipo.route('/tipo')
def tipos():
     return render_template('tipos.html',dataLogin = dataLoginSesion())