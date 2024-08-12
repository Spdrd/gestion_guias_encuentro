import csv
import info_guias as ig


def escribir_csv(guias):
  with open('bdd.csv', 'w', newline='') as csvfile:
    escritor = csv.writer(csvfile, delimiter=',')
    nombre_columnas = ["id", "nombre", "lider", "edad", "telefono"]
    for fecha in ig.fechas:
      nombre_columnas.append("asistencia: " + fecha.strftime("%d-%m-%Y"))
    escritor.writerow(nombre_columnas)
    for guia in guias:
      linea = [guia.id, guia.nombre, guia.lider, guia.edad, guia.telefono]
      for asist in guia.asistencias:
        linea.append(asist.name)
      escritor.writerow(linea)

def leer_csv(guias):
  with open("bdd.csv", "r") as csvfile:
    lector = csv.DictReader(csvfile)
    for linea in lector:
      asistencias = []
      for fecha in ig.fechas:
        pre_enum = linea["asistencia: " + fecha.strftime("%d-%m-%Y")]
        if pre_enum == "CUMPLIDO":
          asistencias.append(ig.Cumplimiento.CUMPLIDO)
        elif pre_enum == "NO_CUMPLIDO":
          asistencias.append(ig.Cumplimiento.NO_CUMPLIDO)
        elif pre_enum == "PENDIENTE":
          asistencias.append(ig.Cumplimiento.PENDIENTE)
      guia = ig.Guia(int(linea["id"]), linea["nombre"], linea["lider"],
                     int(linea["edad"]), linea["telefono"], asistencias)
      guias.append(guia)


def agregar_guia(guias):
  while True:
    print("Ingrese id [-1 para salir]")
    id = int(input())
    if id == -1:
      break
    print("Ingrese nombre")
    nombre = input()
    print("Ingrese lider")
    lider = input()
    print("Ingrese edad")
    edad = int(input())
    print("Ingrese telefono")
    telefono = input()
    guia = ig.Guia(id, nombre, lider, edad, telefono)
    guias.append(guia)

def tomar_asistencia(guias):
  print("Escoger fecha")
  for fecha in ig.fechas:
    print(str(ig.fechas.index(fecha)) + ") " + fecha.strftime("%d-%m-%Y"))

  seleccion_fecha: int = int(input())

  while True:
    print("Ingrese id de guia presente [-1 para salir]")
    guia_presente: int = int(input())
    if guia_presente == -1:
      break
    for guia in guias:
      if guia.id == guia_presente:
        guia.asistencias[seleccion_fecha] = ig.Cumplimiento.CUMPLIDO
        break

def marcar_inasistencias(guias):
  print("Escoger fecha")
  for fecha in ig.fechas:
    print(str(ig.fechas.index(fecha)) + ") " + fecha.strftime("%d-%m-%Y"))

  seleccion_fecha: int = int(input())
  for guia in guias:
    if guia.asistencias[seleccion_fecha] != ig.Cumplimiento.CUMPLIDO:
      guia.asistencias[seleccion_fecha] = ig.Cumplimiento.NO_CUMPLIDO

def imprimir_datos(guias):
  for guia in guias:
    print(guia)

def menu(guias):
  while True:
    print("1) Leer Archivo")
    print("2) Guardar Archivo")
    print("3) Agregar Guia")
    print("4) Tomar Asistencia")
    print("5) Marcar Inasistencias")
    print("6) Imprimir Datos")
    print("9) Salir")
    seleccion = int(input())
    if seleccion == 1:
      leer_csv(guias)
    elif seleccion == 2:
      escribir_csv(guias)
    elif seleccion == 3:
      agregar_guia(guias)
    elif seleccion == 4:
      tomar_asistencia(guias)
    elif seleccion == 5:
      marcar_inasistencias(guias)
    elif seleccion == 6:
      imprimir_datos(guias)
    elif seleccion == 9:
      break
    else:
      print("Selección inválida")
    