#Importando Libreria mysql.connector para conectar Python con MySQL
import mysql.connector
from mysql.connector import Error
from flaskext.mysql import MySQL
import pymysql

def connectionBD():      
      
        mydb = mysql.connector.connect(
            host ="localhost",
            user ="root",
            passwd ="",
            database = "cuadros_c"
        )
        return mydb
    
        try:  
            if mydb.is_connected():        
                print("Conexion exitosa.")
        except Error as ex:
            print("Error durante la conexion:", ex)

