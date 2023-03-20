from tkinter import *
from tkinter import messagebox
from eneviarEmail import enviar

def mostrarmensaje(titulo, mensaje):
    messagebox.showinfo(titulo, mensaje)
def borrar():
    destinatario.set("")
    txtMensaje.delete(1.0, END)
def enviar():
    remitente="josecodtech@gmail.com"
    mensaje=txtMensaje.get(1.0,END)
    enviar(remitente, destinatario.get(), mensaje)
    borrar()
    mostrarmensaje("Aviso","Email enviado")
    
Ventana =  Tk()
Ventana.geometry("640x520")
Ventana.resizable(0, 0)
Ventana.title("Email")
Ventana.config(bg="blue")
destinatario= StringVar()
lblDestinatario= Label(Ventana,text="Destinatario",font=("Aarial",12),bg="white", fg="blue",padx=5,pady=5)
lblDestinatario.place(x=10,y=10,width=100)
txtDestinatario= Entry(Ventana,textvariable=destinatario).place(x=120, y=10,width=400)
lblMensaje= Label(Ventana,text="Mensaje:",font=("Ariel", 12), bg="white", fg="blue", pady=5, padx=5)
lblMensaje.place(x=10, y=50,width=100)
txtMensaje=Text(Ventana)
txtMensaje.place(x=120,y=50,width=400)
btnEnviar=Button(Ventana,text="Enviar",command=enviar).place(x=95,y=480)
btnBorrar=Button(Ventana, text="Borrar",command=borrar).place(x=495,y=480)
txtMensaje.mainloop()
Ventana.mainloop()