from tkinter import *
from tkinter import messagebox

def info():
    messagebox.showinfo("Mensaje","Mensaje desde messagebox")
    
def advertencia():
    messagebox.showwarning("Mensaje","Mensaje de adveretencia")

def pregunta():
    messagebox.askyesno("Mensaje","Quieres continuar?")

ventana= Tk()
ventana.geometry("640x520")
boton1=Button(ventana, text="info",command=info).place(x=20,y=100)
boton2=Button(ventana,text="Advertencia", command=advertencia).place(x=20,y=140)
boton2=Button(ventana,text="pregunta",command=pregunta).place(x=20,y=180)
ventana.mainloop()