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
  var_control = True
  while var_control:
    print("Ingrese id [-1 para salir]")
    id = int(input())
    if id == -1:
      var_control = False 
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
  print("Escoger fecha [-1 para salir]")
  for fecha in ig.fechas:
    print(str(ig.fechas.index(fecha)) + ") " + fecha.strftime("%d-%m-%Y"))
  var_control = True
  while var_control:
    seleccion_fecha = input()
    if seleccion_fecha == "-1":
      var_control = False
      break
    if seleccion_fecha.isnumeric() and int(seleccion_fecha) >= 0 and int(seleccion_fecha) < len(ig.fechas):
      seleccion_fecha = int(seleccion_fecha)
      break
    else:
      print("fecha no valida, intenta otra vez")

  while var_control:
    print("Ingrese id de guia presente [-1 para salir]")
    guia_presente = input()
    if guia_presente.isnumeric() or guia_presente == "-1":
        guia_presente = int(guia_presente)

    if guia_presente == -1:
      var_control = False 
      break
    for guia in guias:
      if guia.id == guia_presente:
        guia.asistencias[seleccion_fecha] = ig.Cumplimiento.CUMPLIDO
        break

def marcar_inasistencias(guias):
  print("Escoger fecha [-1 para salir]")
  for fecha in ig.fechas:
    print(str(ig.fechas.index(fecha)) + ") " + fecha.strftime("%d-%m-%Y"))

  var_control = True
  while var_control:
    seleccion_fecha = input()
    if seleccion_fecha == "-1":
      var_control = False
      break
    if seleccion_fecha.isnumeric() and int(seleccion_fecha) >= 0 and int(seleccion_fecha) < len(ig.fechas):
      seleccion_fecha = int(seleccion_fecha)
      break
    else:
      print("fecha no valida, intenta otra vez")
  if var_control:
    for guia in guias:
      if guia.asistencias[seleccion_fecha] != ig.Cumplimiento.CUMPLIDO:
        guia.asistencias[seleccion_fecha] = ig.Cumplimiento.NO_CUMPLIDO

def imprimir_datos(guias):
  for guia in guias:
    print(guia)

def buscar_guia(guias):
  var_control = True
  while var_control:
    print("Ingrese el nombre o id del guia a buscar [-1 para salir]")
    entrada = input()
    if entrada == "-1":
        var_control = False 
        break
    if entrada.isnumeric():
      for guia in guias:
        if guia.id == int(entrada):
          guia_encontrado = True
          print(f"Guia {guia.nombre} encontrado")
          return guia
    else:
      guias_encontrados = []
      for guia in guias:
        if (entrada.lower()) in (guia.nombre.lower()):          guias_encontrados.append(guia)
      if len(guias_encontrados) > 0:
        print("Escoger Guia")
        for guia in guias_encontrados:
          print(f"{guias_encontrados.index(guia)}) {guia.id} {guia.nombre}")
        seleccion = input()
        if seleccion.isnumeric():
          seleccion = int(seleccion)
          if seleccion >= 0 and seleccion < len(guias_encontrados):
            return guias_encontrados[seleccion]
    print("Guia no encontrado")
  return None

def inspeccionar_guia(guias):
  var_control = True
  while var_control:
    guia = buscar_guia(guias)
    if not (guia is None):
      print("1) Validar porcentaje de asistencias")
      print("-1) Salir")
      entrada = input()
      if entrada.isnumeric():
        entrada = int(entrada)
      if entrada == 1:
        print(guia.reporte_asistencia())
      elif entrada == -1:
        var_control = False 
        break
    else:
      var_control = False

        


def menu(guias):
  var_control = True
  while var_control:
    print("1) Leer Archivo")
    print("2) Guardar Archivo")
    print("3) Agregar Guia")
    print("4) Tomar Asistencia")
    print("5) Marcar Inasistencias")
    print("6) Imprimir Datos")
    print("7) Inspeccionar Guia")
    print("-1) Salir")
    seleccion = input()
    if seleccion.isnumeric() or seleccion == "-1":
        seleccion = int(seleccion)

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
    elif seleccion == 7:
      inspeccionar_guia(guias)
    elif seleccion == -1:
      break
    else:
      print("Selección inválida")
    