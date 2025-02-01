# ventana_texto_corto.py

from tkinter import *

root = Tk()

lbl_nombre = Label(root, text="Nombre")
lbl_nombre.pack(side=LEFT)

txt_nombre = Entry(root)
txt_nombre.pack(side=RIGHT)

root.mainloop()
