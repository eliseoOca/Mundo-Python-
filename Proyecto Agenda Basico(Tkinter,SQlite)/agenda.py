from tkinter import *
from tkinter import messagebox
from baseDatos import *
#crear variables con las posiciones y colores
ANCHO= 560
ALTO = 540
POSX=400
POSY=400
#parametros
anchoAlto = str(ANCHO)+"x"+str(ALTO)
posicionx="+"+str(POSX)
posiciony="+"+str(POSY)
colorVentana="blue"
colorFonde="blue"
colorLetra="white"

def mostrarMensaje(titulo, mensaje):
    messagebox.showinfo(titulo, mensaje)
#boton limpiar datos   
def limpiarDatos():
    nombre.set("")
    apellidos.set("")
    telefono.set("")
    email.set("")
    ID.set("")
    text.delete(1.0, END)
#boton: añadir. funcion guardar datos
def guardar():
    crearTabla()
    if((nombre.get()=="") or (apellidos.get()=="")):
        mostrarMensaje("Error", "Debes rellenar los datos")
    else:
        datos= nombre.get(),apellidos.get(),telefono.get(),email.get()
        mostrarMensaje("Guardar", "Contacto guardado")
        insertar(datos)
        limpiarDatos()
        mostrar()
#boton actualizar. funcion modificar
def actualizar():
    crearTabla()
    if((ID.get() =="") or (ID.get()==0) or (nombre.get()=="")):
        mostrarMensaje("Error", "Debes rellenar los datos")
    else:
        try:
            modificar(ID.get(),nombre.get(),apellidos.get(),telefono.get(),email.get())
            mostrarMensaje("Modificar","Contacto modificado")
            limpiarDatos()
            mostrar()
        except:
            mostrarMensaje("Error", "Indentificador no encontrad0")
#boton borrar.funcion eliminar
def eliminar():
    if(ID.get()=="" or ID.get()== 0):
        mostrarMensaje("Error", "Debes insertar un identificador")
    else:
        try:
            borrar(ID.get())
            mostrarMensaje("Borrar","Contacto borrado")
            limpiarDatos()
            mostrar()
        except:
            mostrarMensaje("Error", "Identificador no encontrado")
#boton consultar. funcion mostrar
def mostrar():
    listado = consultar()
    text.delete(1.0,END)
    text.insert(INSERT, "ID\tNombre\tApellidos\t\tTelefono\tEmail\n")
    for elemento in listado:
        id=elemento[0]
        nombre=elemento[1]
        apellidos=elemento[2]
        telefono=elemento[3]
        email=elemento[4]
        text.insert(INSERT,id)
        text.insert(INSERT,"\t")
        text.insert(INSERT,nombre)
        text.insert(INSERT, "\t")
        text.insert(INSERT,apellidos)
        text.insert(INSERT,"\t\t")
        text.insert(INSERT,telefono)
        text.insert(INSERT,"\t")
        text.insert(INSERT,email)
        text.insert(INSERT,"\n")
        
#boton buscar.funcion buscar

def buscar():
    if((ID.get()=="") or (ID.get()==0)):
        mostrarMensaje("Error", "Debes insertar un indentificador valido")
    else:
        contactos=dameContactos(ID.get())
        for contacto in contactos:
            ID.set(contacto[0])
            nombre.set(contacto[1])
            apellidos.set(contacto[2])
            telefono.set(contacto[3])
            email.set(contacto[4])
        mostrarMensaje("Buscar", "Contacto encontrado")
        
        

#codigo para preparar la ventana y frame interior
ventana=Tk()
ventana.config(bg=colorVentana)#color ventana
ventana.geometry(anchoAlto+posicionx+posiciony)#su parametros
ventana.title("Agenda")#titulo
frame=Frame()
frame.config(width=ANCHO,height=ALTO)
frame.config(bg=colorVentana)
frame.pack()#aca empaquetamos
#variables que vamos a tner los datos de la caja donde metamos los datos en BD
ID= IntVar()
nombre= StringVar()
apellidos=StringVar()
telefono=StringVar()
email=StringVar()
#widgets 
etiquetaID=Label(frame, text="ID: ").place(x=50,y=50)
cajaID = Entry(frame,textvariable=ID).place(x=130,y=50)
etiquetaNombre=Label(frame,text="Nombre: ").place(x=50,y=90)
cajaNombre= Entry(frame, textvariable=nombre).place(x=130,y=90)
etiquetaApellidos = Label(frame,text="Apellidos: ").place(x=50,y=130)
cajaApellidos = Entry(frame,textvariable=apellidos).place(x=130,y=130)
etiquetaTelefono = Label(frame,text="Telefono: ").place(x=50,y=170)
cajaTelefono = Entry(frame,textvariable=telefono).place(x=130,y=170)
etiquetaEmail = Label(frame,text="Email: ").place(x=50,y=210)
cajaEmail = Entry(frame,textvariable=email).place(x=130,y=210)
text=Text(frame)
#AÑADIMOS LOS BOTONES QUE VAMOS A USAR 
text.place(x=50, y=240, width=500, height=200)
botonAñadir=Button(frame,text="Añadir",command=guardar).place(x=150, y=500)
botonBorrar=Button(frame,text="Borrar",command=eliminar).place(x=200, y=500)
botonConsultar=Button(frame,text="Consultar",command=mostrar).place(x=250, y=500)
botonModificar=Button(frame,text="Actualizar",command=actualizar).place(x=320, y=500)
botonBuscar=Button(frame, text="Buscar",command=buscar).place(x=390,y=500)
ventana.mainloop()
