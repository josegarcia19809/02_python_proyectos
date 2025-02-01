# ventana_etiqueta_imagen.py

from tkinter import *

root = Tk()
root.geometry("400x550")
root.config(bg="white")
root.title("Argentina")

lbl_nombre = Label(root, text="Lionel Messi")
lbl_nombre.pack(anchor=CENTER)
# letra azul, fondo blanco Arial 18
lbl_nombre.config(fg="blue",  # Foreground
                  bg="white",  # Background
                  font=("Arial", 18)
                  )
imagen_jugador = PhotoImage(file="messi.png")
Label(root, image=imagen_jugador, bd=0).pack()
root.mainloop()
