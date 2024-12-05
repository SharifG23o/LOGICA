"""
Programa que descompone un numero en factores primos retomando el resultado en forma de cadena
Autor: Programación UQ
Fecha: Abril 2024
Licencia: GNU GPL v3
"""

from apoyo import ingresar_entero, mostrar_mensaje


def main(): 
    n= ingresar_entero("Ingrese el numero a descomponer en factores primos: ")
    descomponer_numero=descomponer(n)
    mostrar_mensaje(descomponer_numero)


def descomponer(n):
	valor=""
	repetir=True
	while repetir:
		if n%2==0:
			valor+="2 "
			n=n//2
		elif n%3==0:
			valor+="3 "
			n=n//3
		elif n%5==0:
			valor+=f"5 "
			n=n//5
		elif n%7==0:
			valor+=f"7 "
			n=n//7
		elif n%11==0:
			valor+=f"11 "
			n=n//11
		else:
			repetir=False
	return valor
    

main()

