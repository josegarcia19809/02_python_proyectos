# ventana_dialogo

from tkinter import *
from tkinter import messagebox
import tkinter.font as font

root = Tk()
root.title("Mostrar caja de diálogo")
root.geometry("400x200+400+200")


def suscribir():
    return messagebox.showinfo(
        "Python",
        "Gracias por tu suscripción"
    )


button_font = font.Font(
    family="Verdana",
    size=16
)

btn_suscribir = Button(
    root,
    text="Suscribirse",
    command=suscribir,
    fg="#34495e",
    font=button_font,
    height=2,
    width=15
)

btn_suscribir.pack(pady=20)
root.mainloop()
