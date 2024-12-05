"""
Programa para determinar la posicion en un equipo de baloncesto segun la altura
Autor: Area de programacion UQ
Fecha: Marzo 2024
Licencia GNU GPL v3
"""

def main():
	altura_cm= ingresar_entero("ingrese la altura del jugador en cm:")
	altura_metros= convertir_cm_mts(altura_cm)
	mensaje_altura= determinar_mensaje_altura(altura_mts)
	mensaje= generar_mensaje(mensaje_altura,altura_cm)
	mostrar_mensaje(mensaje)
def ingresar_entero(mensaje):
	entero= int(input(mensaje)) 
	return entero
def convertir_cm_mts(centimetros):
	metros= centimetros/100
	return metros