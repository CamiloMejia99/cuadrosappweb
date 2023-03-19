from . import queja
from flask import Flask, request, render_template
from conexionBD import *  #Importando conexion BD
from funciones import *  #Importando mis Funciones

from babel import numbers, dates
from datetime import date, datetime, time
from flask_babel import Babel, gettext, refresh; refresh()

app = Flask(__name__)

app.config ['BABEL_DEFAULT_LOCALE'] = 'en'
babel = Babel(app)

def get_locale():
    return request.accept_languages.best_match('en', 'es', 'fr ')
babel = Babel(app, locale_selector=get_locale)

ENVIANOS_SOLICITUD = gettext('ENVIANOS TU SOLICITUD')
Nombre = gettext('Nombre')
Apellido = gettext('Apellido')
Correo = gettext('Correo')
Sexo = gettext('Sexo')
Te_gusta_cuadros = gettext(' ¿Te gusta la paginade C&C "cuadros y mas cuadros"?')
Si = gettext('Si')
No = gettext('No')
Describe_peticion = gettext('Describe tu peticion:')


@queja.route('/quejas') 
def quejas(): 
    return render_template('quejas.html', dataLogin = dataLoginSesion())


@queja.route('/form', methods=['GET', 'POST'])
def registrarForm():
    msg =''
    if request.method == 'POST':
        nombre              = request.form['nombre']
        apellido            = request.form['apellido']
        correo              = request.form['correo']
        sexo                = request.form['sexo']
        likes               = request.form['likes']
        descripcion         = request.form['descripcion']
        
        conexion_MySQLdb = connectionBD()
        cursor           = conexion_MySQLdb.cursor(dictionary=True)
        
        '''
        cursor.execute('INSERT INTO pqrs (nombre, apellido, correo, sexo, likes, descripcion) VALUES (%s, %s, %s, %s, %s, %s)', (nombre, apellido, correo, sexo, likes, descripcion))
        ResultInsert = conexion_MySQLdb.commit()
        '''
            
        sql         = ("INSERT INTO pqrs(nombre, apellido, correo, sexo, likes, descripcion) VALUES (%s, %s, %s, %s, %s, %s)")
        valores     = (nombre, apellido, correo, sexo, likes, descripcion)
        cursor.execute(sql, valores)
        conexion_MySQLdb.commit()
        
        cursor.close() #Cerrando conexion SQL
        conexion_MySQLdb.close() #cerrando conexion de la BD
        msg = 'Registro con exito'
        
        print(cursor.rowcount, "registro insertado")
        print("1 registro insertado, id", cursor.lastrowid)
  
        return render_template('quejas.html', msg='Formulario enviado')
    else:
        return render_template('quejas.html', msg = 'Metodo HTTP incorrecto')

