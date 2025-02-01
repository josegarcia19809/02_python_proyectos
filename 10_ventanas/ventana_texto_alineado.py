# ventana_texto_alineado

from tkinter import *

root = Tk()
root.geometry("400x200")

lbl_nombre = Label(root, text="Nombre")
lbl_nombre.grid(row=0, column=0, sticky=E, padx=15, pady=15)

txt_nombre = Entry(root)
txt_nombre.grid(row=0, column=1, padx=15, pady=15)
txt_nombre.config(justify="right", state="normal")

lbl_apellidos = Label(root, text="Apellidos")
lbl_apellidos.grid(row=1, column=0, sticky=E, padx=15, pady=15)

txt_apellidos = Entry(root)
txt_apellidos.grid(row=1, column=1, padx=15, pady=15)
txt_apellidos.config(justify="center", state="disabled")

root.mainloop()
