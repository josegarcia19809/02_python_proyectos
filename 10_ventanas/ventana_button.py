# ventana_button.py

from tkinter import *

root = Tk()
root.geometry("400x200")
root.config(bg="white")

mensaje = StringVar()


def mostrar_mensaje():
    mensaje.set("Bienvenido")


# Bloque del botón
btn_mensaje = Button(
    root,
    text="Mostrar mensaje",
    command=mostrar_mensaje
)
btn_mensaje.pack(pady=20)

# Bloque de la etiqueta
lbl_saludo = Label(
    root,
    textvariable=mensaje
)
lbl_saludo.pack()

root.mainloop()
