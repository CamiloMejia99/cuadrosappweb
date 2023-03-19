from . import carritocompras
from flask import render_template
from funciones import *  #Importando mis Funciones

from flask import Flask, session, render_template, request, redirect, url_for
from flaskext.mysql import MySQL
import pymysql

from babel import numbers, dates
from datetime import date, datetime, time
from flask_babel import Babel, gettext, refresh; refresh()



app = Flask(__name__)
app.secret_key = "cairocoders-ednalan"
 
mysql = MySQL()
 
# MySQL configurations
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = ''
app.config['MYSQL_DATABASE_DB'] = 'cuadros_c'
app.config['MYSQL_DATABASE_HOST'] = 'localhost'
mysql.init_app(app)

app.config ['BABEL_DEFAULT_LOCALE'] = 'en'
babel = Babel(app)

def get_locale():
    return request.accept_languages.best_match('en', 'es', 'fr ')
babel = Babel(app, locale_selector=get_locale)

#gettext carrito

CARRITO_COMPRAS = gettext('CARRITO DE COMPRAS C&C')
Tus_Cuadros = gettext('Tus Cuadros')
Cantidad = gettext('Cantidad')
Precio_Unitario = gettext('Precio Unitario')
Precio = gettext('Precio')
Estado = gettext('Estado:')
En_existencia = gettext('En Existencia')
Eliminar = gettext('Eliminar')
Cantidad_cuadros = gettext('Cantidad de cuadros')
Total = gettext('Total')
Continue_Comprando = gettext('Continue Comprando')
Pagar = gettext('Pagar')
carrito_vacio = gettext('Tu carrito esta vacio')

@carritocompras.route('/add', methods=['POST'])
def add_product_to_cart():
 cursor = None
 try:
  _quantity = int(request.form['quantity'])
  _code = request.form['code']
  # validate the received values
  if _quantity and _code and request.method == 'POST':
   conn = mysql.connect()
   cursor = conn.cursor(pymysql.cursors.DictCursor)
   cursor.execute("SELECT * FROM product WHERE code=%s", (_code,))
   row = cursor.fetchone()
    
   itemArray = { row['code'] : {'name' : row['name'], 'code' : row['code'], 'quantity' : _quantity, 'price' : row['price'], 'image' : row['image'], 'total_price': _quantity * row['price']}}
    
   all_total_price = 0
   all_total_quantity = 0
    
   session.modified = True
   if 'cart_item' in session:
    if row['code'] in session['cart_item']:
     for key, value in session['cart_item'].items():
      if row['code'] == key:
       old_quantity = session['cart_item'][key]['quantity']
       total_quantity = old_quantity + _quantity
       session['cart_item'][key]['quantity'] = total_quantity
       session['cart_item'][key]['total_price'] = total_quantity * row['price']
    else:
     session['cart_item'] = array_merge(session['cart_item'], itemArray)
 
    for key, value in session['cart_item'].items():
     individual_quantity = int(session['cart_item'][key]['quantity'])
     individual_price = float(session['cart_item'][key]['total_price'])
     all_total_quantity = all_total_quantity + individual_quantity
     all_total_price = all_total_price + individual_price
   else:
    session['cart_item'] = itemArray
    all_total_quantity = all_total_quantity + _quantity
    all_total_price = all_total_price + _quantity * row['price']
    
   session['all_total_quantity'] = all_total_quantity
   session['all_total_price'] = all_total_price
    
   return redirect(url_for('.carrito'))
  else:
   return 'Error while adding item to cart'
 except Exception as e:
  print(e)
 finally:
  cursor.close() 
  conn.close()
   

   
@carritocompras.route('/carrito')
def carrito():
 try:
  conn = mysql.connect()
  cursor = conn.cursor(pymysql.cursors.DictCursor)
  cursor.execute("SELECT * FROM product")
  rows = cursor.fetchall()
  return render_template('carrito.html', carrito=rows)
 except Exception as e:
  print(e)
 finally:
  cursor.close() 
  conn.close()
 
# @carritocompras.route('/empty')
# def empty_cart():
#  try:
#   session.clear()
#   return redirect(url_for('.carrito'))
#  except Exception as e:
#   print(e)
 
@carritocompras.route('/delete/<string:code>')
def delete_product(code):
 try:
  all_total_price = 0
  all_total_quantity = 0
  session.modified = True
   
  for item in session['cart_item'].items():
   if item[0] == code:    
    session['cart_item'].pop(item[0], None)
    if 'cart_item' in session:
     for key, value in session['cart_item'].items():
      individual_quantity = int(session['cart_item'][key]['quantity'])
      individual_price = float(session['cart_item'][key]['total_price'])
      all_total_quantity = all_total_quantity + individual_quantity
      all_total_price = all_total_price + individual_price
    break
   
  if all_total_quantity == 0:
   session.clear()
   return redirect(url_for('.carrito'))
  else:
   session['all_total_quantity'] = all_total_quantity
   session['all_total_price'] = all_total_price
   
  return redirect(url_for('.carrito'))
 except Exception as e:
  print(e)
   
def array_merge( first_array , second_array ):
 if isinstance( first_array , list ) and isinstance( second_array , list ):
  return first_array + second_array
 elif isinstance( first_array , dict ) and isinstance( second_array , dict ):
  return dict( list( first_array.items() ) + list( second_array.items() ) )
 elif isinstance( first_array , set ) and isinstance( second_array , set ):
  return first_array.union( second_array )
 return False
