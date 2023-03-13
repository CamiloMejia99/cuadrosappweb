from . import queja
from flask import render_template
from conexionBD import *  #Importando conexion BD
from funciones import *  #Importando mis Funciones
@queja.route('/quejas')
def quejas():
     return render_template('quejas.html',dataLogin = dataLoginSesion()) 