import glob
import json
import mysql.connector


conexion = mysql.connector.connect(user ='user', password='12345', database='materias')

cursor = conexion.cursor();

files = glob.glob('*.json')
