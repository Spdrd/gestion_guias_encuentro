from enum import Enum
import datetime as dt


class Cumplimiento(Enum):
  CUMPLIDO = 1
  NO_CUMPLIDO = 0
  PENDIENTE = -1


fechas = [
    dt.datetime(day=10, month=8, year=2024),
    dt.datetime(day=17, month=8, year=2024),
    dt.datetime(day=24, month=8, year=2024),
    dt.datetime(day=31, month=8, year=2024),
    dt.datetime(day=7, month=9, year=2024),
    dt.datetime(day=14, month=9, year=2024),
    dt.datetime(day=21, month=9, year=2024),
    dt.datetime(day=28, month=9, year=2024),
    dt.datetime(day=5, month=10, year=2024),
    dt.datetime(day=12, month=10, year=2024),
    dt.datetime(day=19, month=10, year=2024),
    dt.datetime(day=26, month=10, year=2024),
    dt.datetime(day=5, month=10, year=2024),
]


class Guia:

  def __init__(self,
               id,
               nombre,
               lider,
               edad,
               telefono,
               asistencias=[Cumplimiento.PENDIENTE] * 12):
    self.id = id
    self.nombre = nombre
    self.lider = lider
    self.edad = edad
    self.telefono = telefono
    self.asistencias = asistencias

  def __repr__(self):
    return f"{self.id}, {self.nombre}, {self.lider}, {self.edad}, {self.telefono},{self.asistencias}"
