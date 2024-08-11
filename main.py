import info_guias as ig
import funciones as func

if __name__ == "__main__":
  guia = ig.Guia(1, "Juan", "Juan", 25, "55-55-55-55")
  guias = [guia]
  func.escribir_csv(guias)