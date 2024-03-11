"""Modulo para la creacion de formularios"""

import select
from flask_wtf import FlaskForm
from sqlalchemy import null
from wtforms import BooleanField, DateField, FieldList, Form, RadioField, FormField, SelectField, SelectMultipleField
from wtforms import StringField
from wtforms import EmailField
from wtforms import validators


REQUIRED_FIELD_MESSAGE = "El campo es requerido"
INVALID_EMAIL_MESSAGE = "Ingrese un email valido"
VALID_NAME_MESSAGE = "Ingrese un nombre valido"

class AlumnoForm(Form):
    """Formulario para el registro de usuarios"""

    id = StringField("Id")
    nombre = StringField(
        "Nombre",
        [
            validators.DataRequired(message=REQUIRED_FIELD_MESSAGE),
            validators.length(min=4, message=VALID_NAME_MESSAGE),
        ],
    )
    apellidoPaterno = StringField("Apellido Paterno")
    apellidoMaterno = StringField("Apellido Materno")
    email = EmailField(
        "Email",
        [
            validators.DataRequired(message=REQUIRED_FIELD_MESSAGE),
            validators.Email(message=INVALID_EMAIL_MESSAGE),
        ],
    )

class MaestroForm(Form):
    """FORMULARIO PARA EL REGISTRO DE MAESTROS"""

    id = StringField("Id")
    nombre = StringField(
        "Nombre",
        [
            validators.DataRequired(message=REQUIRED_FIELD_MESSAGE),
            validators.length(min=4, message=VALID_NAME_MESSAGE),
        ],
    )
    apellidoPaterno = StringField("Apellido Paterno")
    apellidoMaterno = StringField("Apellido Materno")
    email = EmailField(
        "Email",
        [
            validators.DataRequired(message=REQUIRED_FIELD_MESSAGE),
            validators.Email(message=INVALID_EMAIL_MESSAGE),
        ],
    )
    materia = StringField("Materia")
    email = EmailField(
        "Email",
        [
            validators.DataRequired(message=REQUIRED_FIELD_MESSAGE),
            validators.Email(message=INVALID_EMAIL_MESSAGE),
        ],
    )

class ClienteForm(FlaskForm):
    '''Formulario para el registro de ventas de pizzas'''

    id = StringField("Id")
    nombre = StringField(
        "Nombre",
        [
            validators.DataRequired(message=REQUIRED_FIELD_MESSAGE),
            validators.length(min=4, message=VALID_NAME_MESSAGE),
        ],
    )
    direccion = StringField("Direccion")
    telefono = StringField("Telefono")
    fecha = DateField("")

class VentaPizzasForm(FlaskForm):
    """Formulario para el registro de ventas de pizzas"""

    tamano_pizza = RadioField(
        "Tamaño de la pizza",
        choices=[
            ("Chica", "Chica $40"),
            ("Mediana", "Mediana $80"),
            ("Grande", "Grande $120"),
        ],
    )
    ingrediente_jamon = BooleanField("Jamon $10", render_kw={"value": "Jamon"})
    ingrediente_pina = BooleanField("Piña $10", render_kw={"value": "Pina"})
    ingrediente_pepperoni = BooleanField("Pepperoni $10", render_kw={"value": "Pepperoni"})
    numero_pizzas = StringField(
        "Numero de pizzas",
    )
    subtotal = StringField(
        "SubTotal"
    )

class BusquedaFechaForm(Form):
    """Formulario para la busqueda de alumnos"""

    ano = StringField("Año")
    mes = SelectField(
        "Mes",
        choices=[
            ('', 'Seleccione un mes'),
            ("1", "Enero"),
            ("2", "Febrero"),
            ("3", "Marzo"),
            ("4", "Abril"),
            ("5", "Mayo"),
            ("6", "Junio"),
            ("7", "Julio"),
            ("8", "Agosto"),
            ("9", "Septiembre"),
            ("10", "Octubre"),
            ("11", "Noviembre"),
            ("12", "Diciembre"),
        ],
        default= None
    )
    dia = StringField("Dia")


class BusquedaDiaForm(FlaskForm):
    """Formulario para la busqueda de alumnos"""

    dia_semana = SelectField(
        "Dia",
        choices=[
            ('', 'Seleccione un dia'),
            ("1", "Lunes"),
            ("2", "Martes"),
            ("3", "Miercoles"),
            ("4", "Jueves"),
            ("5", "Viernes"),
            ("6", "Sabado"),
            ("7", "Domingo"),
        ],
    )
