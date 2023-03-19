from flask import Flask,abort, render_template, request
from flask import redirect
from flask import url_for

from tipos import tipo
from precio import precio
from contactos import contacto
from quejas import queja
from carrito import carritocompras
from paginacion import paginacion

from conexionBD import *  #Importando conexion BD
from funciones import *  #Importando mis Funciones

import re
from werkzeug.security import generate_password_hash, check_password_hash


import sentry_sdk
from sentry_sdk.integrations.flask import FlaskIntegration

from babel import numbers, dates
from datetime import date, datetime, time
from flask_babel import Babel, gettext, refresh; refresh()

app = Flask(__name__)

app.secret_key = '97110c78ae51a45af397be6534caef90ebb9b1dcb3380af008f90b23a5d1616bf19bc29098105da20fe'

sentry_sdk.init(
    dsn="https://47b422c23c014fec8d53ccc9dc0e3e61@o4504709798952960.ingest.sentry.io/4504709801443328",
    integrations=[
        FlaskIntegration(),
    ],
    traces_sample_rate=1.0
)

app.config ['BABEL_DEFAULT_LOCALE'] = 'en'
babel = Babel(app)

def get_locale():
    return request.accept_languages.best_match('en', 'es', 'fr ')
babel = Babel(app, locale_selector=get_locale)

@app.route('/debug-sentry')
def trigger_error():
    division_by_zero = 1 / 0
    
@app.route('/generate-error')
def generate_error():
    # Intenta acceder a una variable que no existe
    variable_inexistente = variable_inexistente + 1
    return 'Este error es generado a propósito'    


app.register_blueprint(tipo)
app.register_blueprint(precio)
app.register_blueprint(contacto)
app.register_blueprint(queja)
app.register_blueprint(carritocompras)
app.register_blueprint(paginacion)

#gettext error

Cuadros_y_más_cuadros = gettext('Cuadros y más cuadros')
Solicitud_incorrecta = gettext('Solicitud incorrecta')
UPSSSS = gettext('UPSSSS!!!! Algo salio mal, pagina no encontrada')
sacame = gettext('SACAME DE AQUI!')

#gettext layout

Opciones = gettext('Opciones')
Cuadros = gettext('Cuadros')
Contactanos = gettext('Contactanos')
Quejas = gettext('Quejas y reclamos')
derechos = gettext('Todos los derechos reservados.')
Version = gettext('Version')

# gettext menu 

Inicio = gettext('Inicio')
Cuadros = gettext('CuadrosTipos de cuadros')
Tipos_cuadros = gettext('Tipos de cuadros')
Click_continuar = gettext('Click para continuar')
Contactos = gettext('Contactos')
Comunicate_nosotros = gettext('Comunicate con nosotros')
Detalla_peticion = gettext('Detalla tu peticion')

#gettext pag

Listado_usuarios = gettext('Listado de usuarios')
Datos_usuarios = gettext('Datos de usuarios')

#gettext registro

Ingresar = gettext('Ingresar')
Registrate = gettext('Registrate')
Olvido_contraseña = gettext('Olvido su contraseña?')



# xamp 500
# contraseña 401
# error 404

error_codes = [
    400, 401, 403, 404, 405, 406, 408, 409, 410, 411, 412, 413, 414, 415,
    416, 417, 418, 422, 428, 429, 431, 451, 500, 501, 502, 503, 504, 505
]
for code in error_codes:
    @app.errorhandler(code)
    def client_error(error):
        return render_template('error1.html', error=error), error.code

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
                    session['correo']           = account['correo']
                    session['credencial']       = account['credencial']
                    msg = "Ha iniciado sesión correctamente."
                    return render_template('menu.html', msjAlert = msg, typeAlert=1, dataLogin = dataLoginSesion())
                else:
                    abort(401)
                    # msg = 'Datos incorrectos, por favor verfique!'
                    # return render_template('registro.html', msjAlert = msg, typeAlert=0)
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
        credencial      = request.form['credencial']
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
            abort(401)
        elif not correo or not password or not password or not repite_password:
            msg = 'El formulario no debe estar vacio!'
        else:
            # La cuenta no existe y los datos del formulario son válidos,
            password_encriptada = generate_password_hash(password, method='sha256')
            conexion_MySQLdb = connectionBD()
            cursor = conexion_MySQLdb.cursor(dictionary=True)
            cursor.execute('INSERT INTO users (nombre,correo,credencial,password) VALUES (%s, %s, %s, %s)', ( nombre, correo, credencial, password_encriptada))
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
    session.pop('credencial', None)
    #session.clear()
    #msgClose ="La sesión fue cerrada correctamente"
    return render_template('registro.html')


if __name__ == '__main__':
    # app.register_error_handler(404, pagina_no_encontrada)
    app.run(debug=True, port=5000)
