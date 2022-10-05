import sqlite3
from tkinter import INSERT
from tkinter.tix import InputOnly
conn = sqlite3.connect('estuadiantes.db')
cursor = conn.cursor()
cursor.execute("CREATE TABLE Alumnos (id INT, Nombre TEXT, Apellido INT)")
cursor.execute("INSERT INTO Alumnos VALUES ( 1, 'christian', 'Garcia')")
cursor.execute("INSERT INTO Alumnos VALUES ( 2, 'luz', 'delgado')")
cursor.execute("INSERT INTO Alumnos VALUES ( 3, 'mateo', 'Garcia')")
cursor.execute("INSERT INTO Alumnos VALUES ( 4, 'santiago', 'Garcia')")
cursor.execute("INSERT INTO Alumnos VALUES ( 5, 'hugo', 'Garcia')")
cursor.execute("INSERT INTO Alumnos VALUES ( 6, 'javier', 'Garcia')")
cursor.execute("INSERT INTO Alumnos VALUES ( 7, 'Juan', 'Garcia')")
cursor.execute("INSERT INTO Alumnos VALUES ( 8, 'Soy', 'Garcia')")

conn.commit()
filas = cursor.fetchall()
print (filas)
conn.close()