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
        linea.append(asist.value)
      escritor.writerow(linea)

def leer_csv(guias):
  with open("bdd.csv", "r") as csvfile:
    lector = csv.DictReader(csvfile)
    for linea in lector:
      asistencias = []
      for fecha in ig.fechas:
        asistencias.append(linea[fecha])
      guia = ig.Guia(linea["id"], linea["nombre"], linea["lider"],
                     linea["edad"], linea["telefono"], asistencias)
      guias.append(guia)
