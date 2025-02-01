# ventana_login_v2

from tkinter import *
from tkinter import messagebox

root = Tk()
root.title("Ingresar")
root.geometry("400x200")

usuario = StringVar()
password = StringVar()


def autenticar():
    if usuario.get() == "luis" and password.get() == "123":
        return messagebox.showinfo(
            "Entrada",
            "Bienvenido"
        )
    else:
        return messagebox.showinfo(
            "Entrada",
            "Usuario y/o contraseña no válidos"
        )


lbl_usuario = Label(root, text="Usuario")
lbl_usuario.grid(row=0, column=0, sticky=E, padx=15, pady=15)

txt_usuario = Entry(root, textvariable=usuario)
txt_usuario.grid(row=0, column=1, padx=15, pady=15)
txt_usuario.config(justify="center", state="normal")

lbl_password = Label(root, text="Contraseña")
lbl_password.grid(row=1, column=0, sticky=E, padx=15, pady=15)

txt_password = Entry(root, textvariable=password)
txt_password.grid(row=1, column=1, padx=15, pady=15)
txt_password.config(justify="center", show="*")

btn_autenticar = Button(
    root,
    text="Ingresar",
    command=autenticar
)
btn_autenticar.grid(row=2, column=1, padx=10, pady=10)

root.mainloop()
