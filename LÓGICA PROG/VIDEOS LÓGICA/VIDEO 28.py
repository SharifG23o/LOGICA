"""
Programa que permite contar vocales
autor: programacion UQ
fecha: abril 2024 
licencia: GNU GPL v3
"""


from apoyo import ingresar_texto, mostrar_mensaje

def main():
 frase=ingresar_texto ("Ingrese la frase o respuesta del encuestado: ")
 cantidad_vocales = obtener_cantidad_vocales(frase)
 mensaje_vocales = generar_mensaje_vocales(frase, cantidad_vocales)
 mostrar_mensaje (mensaje_vocales)

def obtener_cantidad_vocales (frase):
 frase=frase.lower()
 cantidad_vocales = frase.count("a") + frase.count("e") + frase.count("i") + frase.count("o") + frase.count("u")
 return cantidad_vocales


def generar_mensaje_vocales (frase, cantidad_vocales):
 mensaje=f"La frase \"{frase}\" tiene {cantidad_vocales} vocales"
 return mensaje
main()
