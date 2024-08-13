from enum import Enum
import datetime as dt


class Cumplimiento(Enum):
  CUMPLIDO = 1
  NO_CUMPLIDO = 0
  PENDIENTE = -1

  def __repr__(self):
    return f"{self.value}"


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
    dt.datetime(day=26, month=10, year=2024)
]


class Guia:

  def __init__(self,
               id: int,
               nombre: str,
               lider: str,
               edad: int,
               telefono: str,
               asistencias = [Cumplimiento.PENDIENTE] * len(fechas)):
    self.id = id
    self.nombre = nombre
    self.lider = lider
    self.edad = edad
    self.telefono = telefono
    self.asistencias = asistencias

  def __repr__(self):
    return f"{self.id}, {self.nombre}, {self.lider}, {self.edad}, {self.telefono},{self.asistencias}"

  def reporte_asistencia(self):
    num_cumplidas = 0
    num_no_cumplidas = 0
    num_pendientes = 0

    for asistencia in self.asistencias:
      if asistencia == Cumplimiento.CUMPLIDO:
        num_cumplidas += 1
      elif asistencia == Cumplimiento.NO_CUMPLIDO:
        num_no_cumplidas += 1
      elif asistencia == Cumplimiento.PENDIENTE:
        num_pendientes += 1
    
    total_sesiones = num_pendientes + num_cumplidas + num_no_cumplidas
    porcentaje_fallas = (num_no_cumplidas / total_sesiones) * 100

    return f"Asistencias: {num_cumplidas}; Fallas: {num_no_cumplidas}; Pendientes: {num_pendientes}; Total: {total_sesiones}; %fallas: {porcentaje_fallas};"
    

