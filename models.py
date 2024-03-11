'''Archivo que contiene el modelo de la tabla alumno'''
import datetime
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Alumno(db.Model):
    '''Modelo de la tabla alumno'''
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(50))
    apellidoPaterno = db.Column(db.String(50))
    apellidoMaterno = db.Column(db.String(50))
    email = db.Column(db.String(50))
    fecha_registro = db.Column(db.DateTime, default=datetime.datetime.now)

class Maestro(db.Model):
    '''Modelo de la tabla maestro'''
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(50))
    apellidoPaterno = db.Column(db.String(50))
    apellidoMaterno = db.Column(db.String(50))
    email = db.Column(db.String(50))
    materia = db.Column(db.String(50))
    fecha_registro = db.Column(db.DateTime, default=datetime.datetime.now)

class Venta(db.Model):
    '''Modelo de la tabla venta'''
    id = db.Column(db.Integer, primary_key=True)
    fecha = db.Column(db.DateTime)
    total = db.Column(db.Float)
    nombre = db.Column(db.String(50))
    direccion = db.Column(db.String(50))
    telefono = db.Column(db.String(50))

class DetalleVenta(db.Model):
    '''Modelo de la tabla detalle_venta'''
    id = db.Column(db.Integer, primary_key=True)
    venta_id = db.Column(db.Integer, db.ForeignKey('venta.id'))
    ingredientes = db.Column(db.String(50))
    tamano = db.Column(db.String(50))
    total = db.Column(db.Float)
