from flask import Flask, redirect, url_for

app = Flask(__name__)


@app.route('/')
def index():
    return "Aprendiendo Flask"


@app.route('/informacion')
def informacion():
    return "<h1>Página de información</h1>"


@app.route('/contacto')
def contacto():
    return "<h1>Mi nombre es José Luis García</h1>"


@app.route('/mostrar-contacto')
def mostrar_contacto():
    return redirect(url_for("contacto")) # POner el nombre de la función de la ruta


@app.route('/lenguajes-de-programacion')
def lenguajes():
    return """
        <h1>Lenguajes de programación</h1>
        <p>Python</p>
        <p>Java</p>
        <p>JavaScript</p>
        <p>C++</p>
        <p>C#</p>
    """


@app.route('/recibir-nombre/<nombre>')
def recibir_nombre(nombre):
    return f"""
        <h1>Página de información</h1>
        <h3>Bienvenido {nombre}</h3>
    """


@app.route('/mostrar-calificacion/<nombre>/<promedio>')
def mostrar_calificacion(nombre, promedio):
    return f"""
        <h1>Página de información</h1>
        <p>Datos del alumno</p>
        <h3>Bienvenido {nombre}</h3>
        <h4>Tu promedio es  {promedio}</h4>
    """


@app.route('/mostrar-precio-producto/<string:producto>/<float:precio>')
def mostrar_precio_producto(producto, precio):
    return f"""
        <h1>Página de información</h1>
        <p>Datos del producto {producto}</p>
        <p>Precio ${precio:,.2f}</p>
    """


@app.route('/mostrar-tipo-vehiculo')
@app.route('/mostrar-tipo-vehiculo/<tipo>')
def mostrar_tipo_vehiculo(tipo=None):
    texto = ""
    if tipo != None:
        texto = f"Tipo de vehiculo {tipo}"
    return f"""
        <h1>Página de información</h1>
        <p>Datos del vehiculo</p>
        {texto}
    """


if __name__ == '__main__':
    app.run()
