""""
Programa para determinar cuantas cajas completas de fruta fresca se necesitan para trasladar un pedido
Autor: Area de programacion UQ
Fecha: Febrero 2024
Licencia: GNU GPL v3
"""


CAPACIDAD_CAJAS=20
MAXIMO_CAJAS=15

def main():
	cantidad_pedido=ingresar_entero("Ingrese cantidad del pedido en Kg: ")
	cantidad_cajas=calcular_cajas(cantidad_pedido,CAPACIDAD_CAJAS)
	mensaje=generar_mensaje(cantidad_pedido,cantidad_cajas,MAXIMO_CAJAS)
	mostrar_mensaje(mensaje)
def ingresar_entero(pregunta):
	entero=int(input(pregunta))
	return entero
def calcular_cajas(cantidad,capacidad):
	cajas=cantidad//capacidad
	return cajas
def generar_mensaje(pedido,cajas,maximo):
	if cajas<=maximo:
		mensaje=f"Para su pedido de {pedido} Kg, se completaran {cajas} cajas con fruta."
	else:
		mensaje="Su pedido no se puede realizar, ah superado el limite de cajas."
	return mensaje
def mostrar_mensaje(mensaje):
	print(mensaje)


main()