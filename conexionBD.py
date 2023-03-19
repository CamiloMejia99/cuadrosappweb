#Importando Libreria mysql.connector para conectar Python con MySQL
# import mysql.connector
# from mysql.connector import Error
# from flaskext.mysql import MySQL
# import pymysql

from flask import render_template,abort
import mysql.connector

def connectionBD():
    try:
        mydb = mysql.connector.connect(
            host ="localhost",
            user ="root",
            password ="",
            db = "cuadros_c"
            )
    except Exception:
        abort(500)
    return mydb
     