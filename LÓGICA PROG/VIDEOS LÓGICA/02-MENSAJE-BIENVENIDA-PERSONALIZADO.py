"""
programa que imprime un mensaje de bienvenida personalizado
autor:Programacion UQ
Fecha: Febrero 2024
LIcencia GNU GPL v3
"""

def main(): 
   nombre = ingresar_texto("Ingrese el nombre del cliente ")
   mensaje = generar_mensaje_bienvenida (nombre)
   mostrar_mensaje(mensaje)


def ingresar_texto(mensaje):
   texto = input(mensaje)
   return texto

def generar_mensaje_bienvenida(nombre):
   mensaje = f"Bienvenid@ {nombre} a la tienda"
   return mensaje

def mostrar_mensaje(mensaje):
   print(mensaje)


main()