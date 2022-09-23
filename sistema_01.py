from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import sqlite3
raiz = Tk()
raiz.title("Aplicacion de Base de datos")
raiz.geometry("600x350")
miId = StringVar
miNombre = StringVar
miCargo = StringVar
miSalario = StringVar

def conexion():
	miConexion=sqlite3.connect("base")
	miCursor.miConexion.cursor()
	try:
		miCursor.execute("""
		CREATE TABLE empleado(
		ID INTEGER PRIMARY KEY AUTOIMCREMENT,
		NOMBRE VARCHAR(50) NOT NULL,
		CARGO VARCHAR(50) NOT NULL,
		SALARIO INT NOT NULL)""")
		messagebox.showinfo("CONEXION", "base de datos creada exitosamente")
	except:
		messagebox.showinfo("CONEXION", "error al crear base de datos")

def limpiarCampos():
	miId.set("")
	miNombre.set("")
	miCargo.set("")
	miSalario.set("")

def crear():
	miConexion=sqlite3.connect("base")
	miCursor=miConexion.cursor()
	try:
		datos=miNombre.get(),miCargo.get(),miSalario.get()
		miCursor.execute("INSERT INTO empleado VALUES(NULL,?,?,?)",(datos))
		miConexion.commint()
	except:
		messagebox.showwarnig("Advertencia","Ocurri error al crear registro")
		pass
	limpiarCampos()
	mostrar()