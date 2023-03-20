from tkinter import *
from PIL import Image

ventana= Tk()
ventana.geometry("640X520")
imagen= ImageTk.PhotoImage(Image.open("icono.png"))
imbLabel= Label(ventana,image=imagen).place(x=100, y=150)
ventana.mainloop()