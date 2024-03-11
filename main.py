PIZZERIA_TEMPLATE = "pizzeria.html"
"""Archivo principal de la aplicacion"""

from flask import Flask, request, render_template, redirect, url_for
from flask_wtf.csrf import CSRFProtect
from config import DevelopmentConfig
from models import DetalleVenta, Venta, db, Alumno, Maestro
from sqlalchemy.exc import SQLAlchemyError
from tokenize import String
from sqlalchemy import extract, func, null

import forms

app = Flask(__name__)
app.config.from_object(DevelopmentConfig)
csrf = CSRFProtect()

detalle_venta = []

@app.errorhandler(404)
def page_not_found(_):
    """Manejador de error 404"""

    return render_template("error.html"), 404


@app.route("/", methods=["GET", "POST"])
def index():
    """Funcion inicial de la aplicacion"""

    return render_template("index.html")


@app.route("/alumnos", methods=["GET", "POST"])
def tabla_alumnos():
    """Funcion para mostrar la tabla de alumnos"""

    alumnos = Alumno.query.all()
    return render_template("alumnos_tabla.html", alumnos=alumnos)


@app.route("/alumnos_form", methods=["GET", "POST"])
def registro_alumnos():
    """Funcion de registro de alumnos"""

    alumno_form = forms.AlumnoForm(request.form)
    if request.method == "POST":
        alumno = Alumno(
            nombre=alumno_form.nombre.data.upper(),
            apellidoPaterno=alumno_form.apellidoPaterno.data.upper(),
            apellidoMaterno=alumno_form.apellidoMaterno.data.upper(),
            email=alumno_form.email.data,
        )
        db.session.add(alumno)
        db.session.commit()

        return redirect(url_for("tabla_alumnos"))

    alumno_form = forms.AlumnoForm()

    return render_template("alumnos.html", form=alumno_form)


@app.route("/alumnos_eliminar", methods=["GET", "POST"])
def alumno_eliminar():
    """Funcion para eliminar un alumno"""

    alumno_form = forms.AlumnoForm(request.form)

    if request.method == "GET":
        alumno = Alumno.query.filter_by(id=request.args.get("id")).first()
        alumno_form.id.data = alumno.id
        alumno_form.nombre.data = alumno.nombre
        alumno_form.apellidoPaterno.data = alumno.apellidoPaterno
        alumno_form.apellidoMaterno.data = alumno.apellidoMaterno
        alumno_form.email.data = alumno.email

    if request.method == "POST":
        alumno = Alumno.query.filter_by(id=request.form["id"]).first()
        db.session.delete(alumno)
        db.session.commit()
        return redirect(url_for("tabla_alumnos"))

    return render_template("alumno_eliminar.html", form=alumno_form)


@app.route("/alumnos_editar", methods=["GET", "POST"])
def alumno_editar():
    """Funcion para editar un alumno"""
    alumno_form = forms.AlumnoForm(request.form)

    if request.method == "GET":
        alumno = Alumno.query.filter_by(id=request.args.get("id")).first()
        alumno_form.id.data = alumno.id
        alumno_form.nombre.data = alumno.nombre
        alumno_form.apellidoPaterno.data = alumno.apellidoPaterno
        alumno_form.apellidoMaterno.data = alumno.apellidoMaterno
        alumno_form.email.data = alumno.email

    if request.method == "POST":
        alumno = Alumno.query.filter_by(id=request.form["id"]).first()
        alumno.nombre = alumno_form.nombre.data
        alumno.apellidoPaterno = alumno_form.apellidoPaterno.data
        alumno.apellidoMaterno = alumno_form.apellidoMaterno.data
        alumno.email = alumno_form.email.data

        db.session.add(alumno)
        db.session.commit()
        return redirect(url_for("tabla_alumnos"))

    return render_template("alumno_editar.html", form=alumno_form)


@app.route("/maestros")
def tabla_maestros():
    """Funcion para mostrar los maestros"""

    maestros = Maestro.query.all()
    return render_template("maestro_tabla.html", maestros=maestros)


@app.route("/maestros_form", methods=["GET", "POST"])
def registro_maestro():
    """Funcion inicial de la aplicacion"""

    maestro_form = forms.MaestroForm(request.form)

    if request.method == "POST":
        maestro = Maestro(
            nombre=maestro_form.nombre.data.upper(),
            apellidoPaterno=maestro_form.apellidoPaterno.data.upper(),
            apellidoMaterno=maestro_form.apellidoMaterno.data.upper(),
            materia=maestro_form.materia.data.upper(),
            email=maestro_form.email.data,
        )
        db.session.add(maestro)
        db.session.commit()

        return redirect(url_for("tabla_maestros"))

    maestro_form = forms.MaestroForm()

    return render_template("maestro.html", form=maestro_form)


@app.route("/maestros_eliminar", methods=["GET", "POST"])
def maestros_eliminar():
    """Funcion para eliminar un alumno"""
    maestro_form = forms.MaestroForm(request.form)

    if request.method == "GET":
        maestro = Maestro.query.filter_by(id=request.args.get("id")).first()
        maestro_form.id.data = maestro.id
        maestro_form.nombre.data = maestro.nombre
        maestro_form.apellidoPaterno.data = maestro.apellidoPaterno
        maestro_form.apellidoMaterno.data = maestro.apellidoMaterno
        maestro_form.email.data = maestro.email
        maestro_form.materia.data = maestro.materia

    if request.method == "POST":

        maestro = Maestro.query.filter_by(id=request.form["id"]).first()
        db.session.delete(maestro)
        db.session.commit()

        return redirect(url_for("tabla_maestros"))

    return render_template("maestro_eliminar.html", form=maestro_form)


@app.route("/maestros_editar", methods=["GET", "POST"])
def maestros_editar():
    """Funcion para eliminar un alumno"""
    maestro_form = forms.MaestroForm(request.form)

    if request.method == "GET":
        maestro = Maestro.query.filter_by(id=request.args.get("id")).first()
        maestro_form.id.data = maestro.id
        maestro_form.nombre.data = maestro.nombre
        maestro_form.apellidoPaterno.data = maestro.apellidoPaterno
        maestro_form.apellidoMaterno.data = maestro.apellidoMaterno
        maestro_form.email.data = maestro.email
        maestro_form.materia.data = maestro.materia

    if request.method == "POST":
        maestro = Maestro.query.filter_by(id=request.form["id"]).first()
        maestro.nombre = maestro_form.nombre.data
        maestro.apellidoPaterno = maestro_form.apellidoPaterno.data
        maestro.apellidoMaterno = maestro_form.apellidoMaterno.data
        maestro.email = maestro_form.email.data
        maestro.materia = maestro_form.materia.data

        db.session.add(maestro)
        db.session.commit()

        return redirect(url_for("tabla_maestros"))

    return render_template("maestro_editar.html", form=maestro_form)

@app.route("/pizzeria", methods=["GET", "POST"])
def ventas_pizzeria():
    """Funcion para mostrar la pagina de la pizzeria"""

    cliente_form = forms.ClienteForm(request.form)
    print(cliente_form.fecha.raw_data)

    if request.method == "POST":
        # Iniciar una transacción
        try:
            # Insertar la venta
            venta = Venta(
                fecha=cliente_form.fecha.data,
                total=calcular_total(),
                nombre=cliente_form.nombre.data,
                direccion=cliente_form.direccion.data,
                telefono=cliente_form.telefono.data,
            )
            db.session.add(venta)
            db.session.flush()  # Esto es necesario para obtener el ID de la venta
            venta_id = venta.id  # Obtener el ID de la venta

            # Insertar los detalles de la venta
            for detalle in detalle_venta:
                detalle_venta_db = DetalleVenta(
                    venta_id=venta_id,
                    ingredientes=detalle["ingredientes"],
                    tamano=detalle["tamano"],
                    total=detalle["subtotal"],
                )
                db.session.add(detalle_venta_db)

            # Confirmar la transacción
            db.session.commit()

            # Limpiar la lista de detalles de venta
            detalle_venta.clear()

        except SQLAlchemyError as e:
            # En caso de error, revertir la transacción
            db.session.rollback()
            print(f"Error al procesar la venta: {e}")

    return render_template(
        PIZZERIA_TEMPLATE,
        venta_form=forms.VentaPizzasForm(),
        cliente_form=forms.ClienteForm(),
        detalle_venta=detalle_venta,
        busqueda_form=forms.BusquedaFechaForm(),
        busqueda_dia_form=forms.BusquedaDiaForm(),
    )


@app.route("/agregar_venta", methods=["GET", "POST"])
def agregar_detalle_venta():
    """DETALLES DE VENTA"""
    detalle_venta_form = forms.VentaPizzasForm(request.form)

    if request.method == "POST":
        ingredientes_seleccionados = []
        ingredientes = ""

        jamon = detalle_venta_form.ingrediente_jamon
        pepperoni = detalle_venta_form.ingrediente_pepperoni
        pina = detalle_venta_form.ingrediente_pina
        tamano_pizza = detalle_venta_form.tamano_pizza
        cantidad = detalle_venta_form.numero_pizzas

        if jamon.data:
            ingredientes += "JAMON "
            ingredientes_seleccionados.append(jamon.label)

        if pepperoni.data:
            ingredientes += "PEPERONI "
            ingredientes_seleccionados.append(pepperoni.label)

        if pina.data:
            ingredientes += "PIÑA "
            ingredientes_seleccionados.append(pina.label)

        subtotal = calcular_subtotal(
            tamano_pizza.data, ingredientes_seleccionados, cantidad.data
        )

        venta_contenido = {
            "ingredientes": ingredientes,
            "tamano": tamano_pizza.data,
            "numero_pizzas": cantidad.data,
            "subtotal": subtotal,
        }

        print(venta_contenido)

        detalle_venta.append(venta_contenido)

        print(detalle_venta)

        total = calcular_total()

    return render_template(
        "pizzeria.html",
        venta_form=forms.VentaPizzasForm(),
        cliente_form=forms.ClienteForm(),
        contenido_venta=detalle_venta,
        busqueda_form=forms.BusquedaFechaForm(),
        busqueda_dia_form=forms.BusquedaDiaForm(),
        total=total,
    )


@app.route("/eliminar_venta")
def eliminar_venta():
    """ELIMINAR VENTA"""

    idx = request.args.get("id")

    detalle_venta.pop(int(idx) - 1)

    return render_template(
        PIZZERIA_TEMPLATE,
        contenido_venta=detalle_venta,
        cliente_form=forms.ClienteForm(),
        busqueda_form=forms.BusquedaFechaForm(),
        busqueda_dia_form=forms.BusquedaDiaForm(),
        venta_form=forms.VentaPizzasForm(),
    )


@app.route("/buscar_venta", methods=["GET", "POST"])
def buscar_venta():
    """FUNCION PARA BUSCAR VENTAS"""

    busqueda_form = forms.BusquedaFechaForm(request.form)

    print(busqueda_form.data)
    mes = request.form["mes"]
    dia = busqueda_form.dia.data
    anio = busqueda_form.ano.data

    print(f"Mes: {mes}, Dia: {dia}, Año: {anio}")
    busqueda = []

    if request.method == "POST":
        if anio and mes and dia:
            busqueda = buscar_venta_fecha(f"{anio}-{mes}-{dia}")
        if anio and mes and not dia:
            busqueda = buscar_venta_mes_anio(mes, anio)
        if anio and not mes and not dia:
            busqueda = buscar_ventas_anio(anio)
        if anio and not mes and dia:
            busqueda = buscar_venta_anio_dia(anio, dia)
        if not anio and mes is not null and mes != "" and not dia:
            busqueda = buscar_ventas_mes(mes)
        if not anio and not mes and dia:
            busqueda = buscar_ventas_dia(dia)

    return render_template(
        "pizzeria.html",
        venta_form=forms.VentaPizzasForm(),
        cliente_form=forms.ClienteForm(),
        busqueda_form=forms.BusquedaFechaForm(),
        busqueda_dia_form=forms.BusquedaDiaForm(),
        busqueda_venta=busqueda,
    )


@app.route("/buscar_venta_dia", methods=["GET", "POST"])
def buscar_dia():
    """FUNCION PARA BUSCAR VENTAS"""

    if request.method == "POST":
        dia_semana = request.form["dia_semana"]
        if dia_semana is not None and dia_semana != '':
            busqueda = buscar_ventas_dia_semana(dia_semana)

    return render_template(
        "pizzeria.html",
        venta_form=forms.VentaPizzasForm(),
        cliente_form=forms.ClienteForm(),
        busqueda_form=forms.BusquedaFechaForm(),
        busqueda_dia_form=forms.BusquedaDiaForm(),
        busqueda_venta=busqueda,
    )


def calcular_subtotal(tamano, ingredientes, cantidad):
    """FUNCION PARA CALCULAR EL SUBTOTAL"""
    # Diccionario con los precios de los tamaños de pizza
    precios_tamanos = {"Chica": 40, "Mediana": 80, "Grande": 120}
    # Costo base de la pizza según el tamaño seleccionado
    costo_base = precios_tamanos.get(tamano, 0)
    # Costo adicional por cada ingrediente seleccionado
    costo_ingredientes = len(ingredientes) * 10

    # Subtotal de la venta (costo base + costo ingredientes) multiplicado por la cantidad
    subtotal = costo_base + costo_ingredientes
    subtotal = subtotal * int(cantidad)
    print(subtotal)

    return subtotal


def calcular_total():
    """CALCULAR TOTAL"""
    total = 0
    if detalle_venta:
        for detalle in detalle_venta:
            total += detalle["subtotal"]

    return total

def buscar_ventas_mes(mes):
    """FUNCION PARA BUSCAR VENTAS"""
    print("MES " + mes)
    ventas = Venta.query.filter(extract("month", Venta.fecha) == int(mes)).all()
    return ventas


def buscar_ventas_dia(dia):
    """FUNCION PARA BUSCAR VENTAS"""
    print("DIA " + dia)
    ventas = Venta.query.filter(extract("day", Venta.fecha) == int(dia)).all()
    return ventas


def buscar_ventas_anio(anio):
    """FUNCION PARA BUSCAR VENTAS"""
    print("ANIO: " + anio)
    ventas = Venta.query.filter(extract("year", Venta.fecha) == int(anio)).all()
    return ventas

def buscar_ventas_dia_semana(dia_semana):
    """FUNCION PARA BUSCAR VENTAS"""
    print("DIA SEMANA: " + dia_semana)
    ventas = ventas = Venta.query.filter(
        func.dayofweek(Venta.fecha) == dia_semana
    ).all()
    return ventas

def buscar_venta_fecha(fecha):
    """FUNCION PARA BUSCAR VENTAS"""
    print("FECHA: " + fecha)
    ventas = Venta.query.filter_by(fecha=fecha).all()
    return ventas

def buscar_venta_mes_dia(mes, dia):
    """FUNCION PARA BUSCAR VENTAS"""
    print("MES: " + mes)
    print("DIA: " + dia)
    ventas = Venta.query.filter(
        extract("month", Venta.fecha) == int(mes), extract("day", Venta.fecha) == int(dia)
    ).all()
    return ventas

def buscar_venta_mes_anio(mes, anio):
    """FUNCION PARA BUSCAR VENTAS"""
    print("MES: " + mes)
    print("ANIO: " + anio)
    ventas = Venta.query.filter(
        extract("month", Venta.fecha) == int(mes), extract("year", Venta.fecha) == int(anio)
    ).all()
    return ventas

def buscar_venta_anio_dia(anio, dia):
    """FUNCION PARA BUSCAR VENTAS"""
    print("ANIO: " + anio)
    print("DIA: " + dia)
    ventas = Venta.query.filter(
        extract("year", Venta.fecha) == int(anio), extract("day", Venta.fecha) == int(dia)
    ).all()
    return ventas

if __name__ == "__main__":
    csrf.init_app(app)
    db.init_app(app)
    with app.app_context():
        db.create_all()
    app.run(port=8001)
