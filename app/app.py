from flask import Flask, render_template, request
from flask import redirect
from flask import url_for

from tipos import tipo
from precio import precio
from contactos import contacto
from quejas import queja

from conexionBD import *  #Importando conexion BD
from funciones import *  #Importando mis Funciones

import re
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)

app.register_blueprint(tipo)
app.register_blueprint(precio)
app.register_blueprint(contacto)
app.register_blueprint(queja)

@app.errorhandler(404)
def page_not_found(error):
    return (render_template("error.html", error="Página no encontrada..."),
            404)

app.secret_key = '97110c78ae51a45af397be6534caef90ebb9b1dcb3380af008f90b23a5d1616bf19bc29098105da20fe'

#inicio de sesion
@app.route('/sesion', methods=['GET', 'POST'])
def loginUser():
    conexion_MySQLdb = connectionBD()
    if 'conectado' in session:
        return render_template('menu.html', dataLogin = dataLoginSesion())
    else:
        msg = ''
        if request.method == 'POST' and 'correo' in request.form and 'password' in request.form:
            correo   = str(request.form['correo'])
            password   = str(request.form['password'])

            # Comprobando si existe una cuenta
            cursor = conexion_MySQLdb.cursor(dictionary=True)
            cursor.execute("SELECT * FROM users WHERE correo = %s", [correo])
            account = cursor.fetchone()

            if account:
                if check_password_hash(account['password'],password):
                    # Crear datos de sesión, para poder acceder a estos datos en otras rutas
                    session['conectado']        = True
                    session['nombre']           = account['nombre']
                    session['correo']          = account['correo']

                    msg = "Ha iniciado sesión correctamente."
                    return render_template('menu.html', msjAlert = msg, typeAlert=1, dataLogin = dataLoginSesion())
                else:
                    msg = 'Datos incorrectos, por favor verfique!'
                    return render_template('registro.html', msjAlert = msg, typeAlert=0)
            else:
                return render_template('registro.html', msjAlert = msg, typeAlert=0)
    return render_template('registro.html', msjAlert = 'Debe iniciar sesión.', typeAlert=0)


#Registrando una cuenta de Usuario
@app.route('/registro', methods=['GET', 'POST'])
def registerUser():
    msg = ''
    conexion_MySQLdb = connectionBD()
    if request.method == 'POST':
        nombre          = request.form['nombre']
        correo          = request.form['correo']
        password        = request.form['password']
        repite_password = request.form['repite_password']
        #current_time = datetime.datetime.now()

        # Comprobando si ya existe la cuenta de Usuario con respecto al email
        cursor = conexion_MySQLdb.cursor(dictionary=True)
        cursor.execute('SELECT * FROM users WHERE correo = %s', (correo,))
        account = cursor.fetchone()
        cursor.close() #cerrrando conexion SQL

        if account:
            msg = 'Ya existe un usuario con esta nombre!'
        elif password != repite_password:
            msg = 'Disculpa, las clave no coinciden!'
        elif not correo or not password or not password or not repite_password:
            msg = 'El formulario no debe estar vacio!'
        else:
            # La cuenta no existe y los datos del formulario son válidos,
            password_encriptada = generate_password_hash(password, method='sha256')
            conexion_MySQLdb = connectionBD()
            cursor = conexion_MySQLdb.cursor(dictionary=True)
            cursor.execute('INSERT INTO users (nombre,correo,password) VALUES (%s, %s, %s)', ( nombre, correo, password_encriptada))
            conexion_MySQLdb.commit()
            cursor.close()
            msg = 'Cuenta creada correctamente!'

        return render_template('registro.html', msjAlert = msg, typeAlert=1)
    return render_template('registro.html', dataLogin = dataLoginSesion(), msjAlert = msg, typeAlert=0)
    #return render_template('public/layout.html', dataLogin = dataLoginSesion(), msjAlert = msg, typeAlert=0)

@app.route('/')
def index():
    return render_template('registro.html')

@app.route('/reg')
def reg():
    return render_template('registro.html')

@app.route('/login')
def login():
    if 'conectado' in session:
        return render_template('menu.html', dataLogin = dataLoginSesion())
    else:
        return render_template('registro.html')

@app.route('/logout')
def logout():
    msgClose = ''
    # Eliminar datos de sesión, esto cerrará la sesión del usuario
    session.pop('conectado', None)
    session.pop('nombre', None)
    session.pop('correo', None)
    #session.clear()
    #msgClose ="La sesión fue cerrada correctamente"
    return render_template('registro.html')


if __name__ == '__main__':
    # app.register_error_handler(404, pagina_no_encontrada)
    app.run(debug=True, port=5000)
