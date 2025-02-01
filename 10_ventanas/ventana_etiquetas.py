# ventana_etiquetas.py
from tkinter import *

root = Tk()
root.geometry("400x200")
root.title("Bienvenido")

label = Label(root, text="Curso de Python")
label.pack()

Label(root, text="Curso de Java").pack()

lbl_saludo = Label(root, text="Curso de C++")
lbl_saludo.pack(anchor=CENTER)
lbl_saludo.config(fg="white",  # Foreground
                  bg="red",  # Background
                  font=("Arial", 24)
                  )

root.mainloop()
