from tkinter import *
import tkinter.font as font

imagenes = ["image-1.png", "image-2.png", "image-3.png", "image-4.png", "image-5.png"]
textos = [
    "Luis busca en el mapa",
    "María examina los hongos",
    "Antonio toca la guitarra",
    "Raquel está pescando",
    "Roberto ya se perdió"
]

indice = 0

root = Tk()
root.geometry("660x600+300+100")
root.config(bg="white")
root.title("Hiking")

titulo = StringVar()


def cambiar_imagen():
    global imagenes
    global imagen_personaje
    global imagen_personaje_ajustada
    imagen_personaje = PhotoImage(file=imagenes[indice])
    imagen_personaje_ajustada = imagen_personaje.subsample(2)
    lbl_imagen.config(image=imagen_personaje_ajustada)
    lbl_imagen.image = imagen_personaje_ajustada


def cambiar_titulo():
    titulo.set(textos[indice])


def anterior():
    global indice
    indice = indice - 1
    if indice < 0:
        indice = 4

    cambiar_imagen()
    cambiar_titulo()


def siguiente():
    global indice
    indice = indice + 1
    if indice > 4:
        indice = 0

    cambiar_imagen()
    cambiar_titulo()


cambiar_titulo()
lbl_titulo = Label(root, textvariable=titulo)
lbl_titulo.grid(row=0, column=1, sticky="nsew", padx=15, pady=15)
lbl_titulo.config(
    fg="blue",
    bg="white",
    font=("Calibri", 32)
)

imagen_personaje = PhotoImage(file=imagenes[indice])
imagen_personaje_ajustada = imagen_personaje.subsample(2)
lbl_imagen = Label(root, image=imagen_personaje_ajustada, bd=0)
lbl_imagen.grid(row=1, column=1, sticky=E, padx=5, pady=5)

button_font = font.Font(
    family="Verdana",
    size=36
)

btn_anterior = Button(
    root,
    text="<",
    font=button_font,
    command=anterior
)
btn_anterior.grid(row=1, column=0, padx=10, pady=10)

btn_siguiente = Button(
    root,
    text=">",
    font=button_font,
    command=siguiente
)
btn_siguiente.grid(row=1, column=2, padx=10, pady=10)

root.mainloop()
