# ventana_login_v1

# Usuario Contraseña

from tkinter import *

root = Tk()
root.geometry("400x200")

lbl_usuario = Label(root, text="Usuario")
lbl_usuario.grid(row=0, column=0, sticky=E, padx=15, pady=15)

txt_usuario = Entry(root)
txt_usuario.grid(row=0, column=1, padx=15, pady=15)
txt_usuario.config(justify="center", state="normal")

lbl_password = Label(root, text="Contraseña")
lbl_password.grid(row=1, column=0, sticky=E, padx=15, pady=15)

txt_password = Entry(root)
txt_password.grid(row=1, column=1, padx=15, pady=15)
txt_password.config(justify="center", show="*")

root.mainloop()
