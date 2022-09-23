from asyncio.windows_events import NULL
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

def mostrar():
	miConexion=sqlite3.connect("base")
	miCursor=miConexion.cursor()
	registro=tree.get_children()
	for elemento in registro:
		tree.delete(elemento)
	try:
		miCursor.execute("SELECT * FROM empleado")
		for fila in miCursor:
			tree.insert("",0,text=fila[0], values=(fila[1],fila[2],fila[3]))
	except:
		pass

def elimanar():
	miConexion=sqlite3.connect("base")
	miCursor=miConexion.cursor()
	if miCursor.askyesno(message="Datos seran eliminados permanentemente",title="Advertencia"):
		miCursor.execute("DROP TABLE empleado")
	else:
		pass

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

# dibujar tabla 
tree.tkk.Treeview(height=10, colmns=('#0','#1','#2'))
tree.place(x=0,y=130)
tree.column('#0', width=180)
tree.heading('#0', text='ID', anchor=CENTER)
tree.heading('#1', text='Nombres', anchor=CENTER)
tree.heading('#2', text='Cargo', anchor=CENTER)
tree.column('#3', width=180)
tree.heading('#3', text='Salario', anchor=CENTER)

def seleccionar(event):
	item=tree.identify('item', event.x event.y)
	miId.set(tree.item(item,'text'))
	miNombre.set(tree.item(item,'Values')[0])
	miCargo.set(tree.item(item,'Values')[1])
	miSalario.set(tree.item(item,'Values')[2])

tree.bind("<Dou")