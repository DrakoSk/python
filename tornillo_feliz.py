from tkinter import *
from tkinter import messagebox as MessageBox

def home():
    """funcion esta vacio """


def add():
    """funcion esta vacio """


def info():
    """funcion esta vacio """



def Calculo():
#En esta funcion esta la logica de calcular el total y subtotal de ventas asignado
 #por un precio por el usuario junto con la declaracion de try- except.

    try:
    #Accediendo a los valores mediante el metodo get de cantidad y precio.
        cant=int(obtenerCantidad.get());
        cant1=int(tCantidad1.get());
        cant2=int(obtenerCantidad2.get());
        prec=float(obtenerPrecio.get());
        prec1=float(obtenerPrecio1.get());
        prec2=float(obtenerPrecio2.get());
    #calculo del subtotal de ventas
        subt=(cant*prec);
        subt1=(cant1*prec1);
        subt2=(cant2*prec2);
    #calculo del total de ventas
        totl = (subt+subt1+subt2);
    #valores mediane el metodo set a subtotal y total     
        obtenerSubtotal.set(str(subt));
        obtenerSubtotal1.set(str(subt1));
        obtenerSubtotal2.set(str(subt2));
    #valores mediane el metodo set a total
        obtenerTotal.set(str(totl));
        

    except ValueError:
            MessageBox.showinfo("AVISO IMPORTANTE","""En la columna Cantidad o Precio hay valores incorrectos.
Ingrese solo numeros y evite dejar celdas vacias.

                        ╔╦══════════════════╦╗ 
                                Necesitas Ayuda.
                        ╚╩══════════════════╩╝

Puede ingresar solo los codigos de productos y el sistema te arrojara los precios""");

    
def Codigos():
    """ obtiene por condicionales los valores predeterminado para la casilla codigo de producto, descripcion, unidad y precio"""
#Accediendo a los valores mediante el metodo get de codigo, descripcion, unidad y precio
    try:
        codg=int(obtenerCodigo.get());
        codg1=int(obtenerCodigo1.get());
        codg2=int(obtenerCodigo2.get());
        desc=obtenerDescripcion.get();
        desc1=obtenerDescripcion1.get();
        desc2=obtenerDescripcion2.get();

        prec=obtenerPrecio.get();
        prec1=obtenerPrecio1.get();
        prec2=obtenerPrecio2.get();

        uni=obtenerUnidad.get();
        uni1=obtenerUnidad1.get();
        uni2=obtenerUnidad2.get();

#obteniendo valores predefinidos por condicionales para codigo de producto, descripcion, unidad y precio

#condicion para la primera columna de codigo de producto, precio y unidad
        if codg>1 and codg<10:
            desc="Stock"
            prec=15
            uni = "Kilogramos"
        elif codg>10 and codg <30:
            desc="sin oferta"
            prec=30
            uni= "Metros"
        else:
            desc= "oferta"
            prec=50
            uni ="Litros"

#segunda columna de codigo de producto, precio y unidad
        if codg1>1 and codg<10:
            desc1="Stock"
            prec1=60
            uni1 = "Kilos"
        elif codg1>10 and codg <30:
            desc1="sin oferta"
            prec1= 80
            uni1= "Metros"
        else:
            desc1= "oferta"
            prec1=90
            uni1 ="Litros"

    #tercera celda de codigo de producto, precio y unidad
        if codg2>1 and codg<10:
            desc2="Stock"
            prec2=90
            uni2 ="Litros"
        elif codg2>10 and codg <30:
            desc2="sin oferta"
            prec2=120
            uni2="Kilos"
        else:
            desc2= "oferta"
            prec2=190
            uni2= "Metros"

    #fijando los valores mediane el metodo set a precio, descripcion, codigo y unidad
        obtenerPrecio.set(str(prec));
        obtenerPrecio1.set(str(prec1));
        obtenerPrecio2.set(str(prec2));
        
        obtenerDescripcion.set(str(desc));
        obtenerDescripcion1.set(str(desc1));
        obtenerDescripcion2.set(str(desc2));

        obtenerCodigo.set(str(codg));
        obtenerCodigo1.set(str(codg1));
        obtenerCodigo2.set(str(codg2));

        obtenerUnidad.set(str(uni));
        obtenerUnidad1.set(str(uni1));
        obtenerUnidad2.set(str(uni2));
    except ValueError:
            MessageBox.showinfo("AVISO IMPORTANTE","""En la columna Cod_Prod ingresar un numero valido.
Evite dejar casillas vacios
    
NOTA: los codigos de productos solo son numeros.""");


def Limpiar():
    """ Esta funcion limpia o reinicia los valores a cero, permitiendo ingresar los valores nuevos por el usuario"""
    #Accediendo a los valores mediante el metodo get a todos las celdas del segundo frame
    obtenerCodigo.set("");
    obtenerCodigo1.set("");
    obtenerCodigo2.set("");
    obtenerDescripcion.set("");
    obtenerDescripcion1.set("");
    obtenerDescripcion2.set("");
    obtenerUnidad.set("");
    obtenerUnidad1.set("");
    obtenerUnidad2.set("");
    obtenerCantidad.set("");
    obtenerCantidad1.set("");
    obtenerCantidad2.set("");
    obtenerPrecio.set("");
    obtenerPrecio1.set("");
    obtenerPrecio2.set("")
    obtenerSubtotal.set("");
    obtenerSubtotal1.set("");
    obtenerSubtotal2.set("");
    obtenerTotal.set("");
    tDni.focus();


root = Tk() #root = nombre de mi raiz
root.title('Ferreteria El tornillo feliz_jhon saul_____[SK]') # nombre del titulo de mi ventana
root.config(bg= "#C6C6BC") # background o fondo de mi ventana
root.iconbitmap('imagen.ico')# imagen con el icono de mi ventana
root.resizable(False,False) #Evita que se expanda mi ventana


miFrame = Frame(root)# primer frame
miFrame.pack() #empaquetando
miFrame.config(bg = "#C6C6BC")#fondo de mi primer frame
miFrame.config(cursor = "cross") #miniatura del raton (cruz)

#Insertamos los widgets
#label titulo
lDni = Label(miFrame, text='Ferretria El tornillo Feliz', font=("Forte", 30),bg= "#C6C6BC" )
lDni.grid(row=0, column=2, pady=10, padx=10)

#Label y entry de DNI --------------------------------
obtenerDni=StringVar() 
lDni = Label(miFrame, text='DNI:')
lDni.grid(row=5, column=0, sticky='e', pady=5, padx=5)
tDni = Entry(miFrame,textvariable=obtenerDni)
tDni.grid(row=5, column=1, pady=5, padx=5)

#Label y entry Apellido --------------------------------
obtenerApellido=StringVar() 
lApellido = Label(miFrame, text='Apellido:')
lApellido.grid(row=6, column=0, sticky='e', pady=5, padx=5)
tApellido = Entry(miFrame,textvariable=obtenerApellido)
tApellido.grid(row=6, column=1, pady=5, padx=5)
#Label y entry Nombre --------------------------------
obtenerNombre=StringVar()
lNombre = Label(miFrame, text='Nombre:')
lNombre.grid(row=6, column=2, sticky='e', pady=1, padx=1)
tNombre = Entry(miFrame,textvariable=obtenerNombre)
tNombre.grid(row=6, column=3, pady=5, padx=5)
#Label y entry Dieccion --------------------------------
obtenerDir=StringVar() 
lDireccion = Label(miFrame, text='Direccion:')
lDireccion.grid(row=7, column=0, sticky='e', pady=5, padx=5)
tDireccion = Entry(miFrame,textvariable=obtenerDir)
tDireccion.grid(row=7, column=1, columnspan=3, sticky='we',pady=5, padx=5)
#Label y entry Telefono --------------------------------
obtenerTel=StringVar() 
lTel = Label(miFrame, text='Telefono:')
lTel.grid(row=8, column=0, sticky='e', pady=5, padx=5)
tTel = Entry(miFrame,textvariable=obtenerTel)
tTel.grid(row=8, column=1,columnspan=3, sticky='we', pady=5, padx=5)

#segundo frame
miFrame1 = Frame(root)
miFrame1.pack()

#nombre de mis variables(CODIGO)
obtenerCodigo = StringVar()
obtenerCodigo1 = StringVar()
obtenerCodigo2 = StringVar()
#Label y entry,s Código producto -----------------------
lCodigo = Label(miFrame1, text='Cod_Prod')
lCodigo.grid(row=9, column=0,sticky='e', pady=5, padx=5)
tCodigo1 = Entry(miFrame1, width=7, textvariable =obtenerCodigo)
tCodigo1.grid(row=10, column=0, pady=5, padx=5)
tCodigo2 = Entry(miFrame1, width=7,textvariable =obtenerCodigo1 )
tCodigo2.grid(row=11, column=0, pady=5, padx=5)
tCodigo3 = Entry(miFrame1, width=7,textvariable =obtenerCodigo2)
tCodigo3.grid(row=12, column=0, pady=5, padx=5)


#nombres de mis variables (DESCRIPCION)
obtenerDescripcion = StringVar() 
obtenerDescripcion1 =StringVar()
obtenerDescripcion2 =StringVar()
#Label y entry,s Descripcion ---------------------------
lDes = Label(miFrame1, text='Descripcon')
lDes.grid(row=9, column=1,sticky='ew', pady=5, padx=5)
tDes1 = Entry(miFrame1, width=7, state="readonly",textvariable = obtenerDescripcion)
tDes1.grid(row=10, column=1, pady=5, padx=5)
tDes2 = Entry(miFrame1, width=7, state="readonly",textvariable = obtenerDescripcion1)
tDes2.grid(row=11, column=1, pady=5, padx=5)
tDes3 = Entry(miFrame1, width=7, state="readonly",textvariable = obtenerDescripcion2)
tDes3.grid(row=12, column=1, pady=5, padx=5)

#nombres de mi variable (UNIDAD)
obtenerUnidad = StringVar() 
obtenerUnidad1 = StringVar()
obtenerUnidad2 = StringVar()
#Label y entry,s Unidad --------------------------------
lUni = Label(miFrame1, text='Unidad')
lUni.grid(row=9, column=2,sticky='ew', pady=5, padx=5)
tUni1 = Entry(miFrame1, width=7, state="readonly", textvariable = obtenerUnidad)
tUni1.grid(row=10, column=2, pady=5, padx=5)
tUni2 = Entry(miFrame1, width=7, state="readonly",textvariable = obtenerUnidad1 )
tUni2.grid(row=11, column=2, pady=5, padx=5)
tUni3 = Entry(miFrame1, width=7, state="readonly",textvariable = obtenerUnidad2)
tUni3.grid(row=12, column=2, pady=5, padx=5)

#nombres de mi variable (CANTIDAD)
obtenerCantidad = StringVar()
obtenerCantidad1 = StringVar()
obtenerCantidad2 = StringVar()
#Label y entry,s Cantidad ------------------------------
lCantidad = Label(miFrame1, text='Cantidad')
lCantidad.grid(row=9, column=3,sticky='ew', pady=5, padx=5)
tCantidad1 = Entry(miFrame1, width=7, textvariable = obtenerCantidad)
tCantidad1.grid(row=10, column=3, pady=5, padx=5)
tCantidad2 = Entry(miFrame1, width=7, textvariable = obtenerCantidad1)
tCantidad2.grid(row=11, column=3, pady=5, padx=5)
tCantidad3 = Entry(miFrame1, width=7, textvariable = obtenerCantidad2)
tCantidad3.grid(row=12, column=3, pady=5, padx=5)

#Nombres de mis variables (PRECIO)
obtenerPrecio = StringVar()
obtenerPrecio1 = StringVar()
obtenerPrecio2 = StringVar()
#Label y entry,s Precio --------------------------------
lPrecio = Label(miFrame1, text='Precio')
lPrecio.grid(row=9, column=4,sticky='ew', pady=5, padx=5)
tPrecio1 = Entry(miFrame1, width=7,textvariable = obtenerPrecio)
tPrecio1.grid(row=10, column=4, pady=5, padx=5)
tPrecio2 = Entry(miFrame1, width=7,textvariable = obtenerPrecio1)
tPrecio2.grid(row=11, column=4, pady=5, padx=5)
tPrecio3 = Entry(miFrame1, width=7,textvariable = obtenerPrecio2)
tPrecio3.grid(row=12, column=4, pady=5, padx=5)

#nombre de mi variable (SUB TOTAL)
obtenerSubtotal = StringVar()
obtenerSubtotal1 = StringVar()
obtenerSubtotal2 = StringVar()
#Label y entry,s Subtotal ------------------------------
lSubtotal = Label(miFrame1, text='Subtotal')
lSubtotal.grid(row=9, column=5,sticky='ew', pady=5, padx=5)
tSubtotal1 = Entry(miFrame1, width=7, state="readonly",textvariable = obtenerSubtotal)
tSubtotal1.grid(row=10, column=5, pady=5, padx=5)
tSubtotal2 = Entry(miFrame1, width=7, state="readonly",textvariable = obtenerSubtotal1)
tSubtotal2.grid(row=11, column=5, pady=5, padx=5)
tSubtotal3 = Entry(miFrame1, width=7, state="readonly",textvariable = obtenerSubtotal2)
tSubtotal3.grid(row=12, column=5, pady=5, padx=5)

#Label y entry,s Total --------------------------------
obtenerTotal = StringVar() # Nombre de la variable de total
lTotal = Label(miFrame1, text='Total',font=("Franklin Gothic Demi Cond", 12),bg= "#CD6155")
lTotal.grid(row=12, column=6,sticky='ew', pady=5, padx=5)
tTotal = Entry(miFrame1, width=7, textvariable = obtenerTotal)
tTotal.grid(row=12, column=7, pady=5, padx=5)
#Boton guardar -----------------------------------------<=========
guardar=Button(miFrame1, text='Calcular',font=("Franklin Gothic Demi Cond", 15),bg= "#AED6F1", command=Calculo)
guardar.grid(row=13, column=5, pady=10, padx=10)

#boton Informacion
guardar=Button(miFrame1, text='Informacion',font=("Franklin Gothic Demi Cond", 12),bg= "#FAD7A0", command=Codigos)
guardar.grid(row=13, column=1, pady=5, padx=5)

#boton Limpiar
guardar=Button(miFrame1, text='Limpiar', font=("Franklin Gothic Demi Cond", 12),bg= "#EB984E", command= Limpiar)
guardar.grid(row=13, column=0, pady=5, padx=5)

#menu
Mi_Menu = Menu(root)
root.config(menu = Mi_Menu)
 
submenu = Menu(Mi_Menu, tearoff = 0)
Mi_Menu.add_cascade(label = "Archivo", menu = submenu)
 
#sub menus 
submenu.add_cascade(label= "Inicio", command = home)
submenu.add_command(label= "Añadir", command = add)
submenu.add_command(label="informacion", command = info)
submenu.add_separator()
submenu.add_command(label="Salir", command = quit)

root.mainloop()