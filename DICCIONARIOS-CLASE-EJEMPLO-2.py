"""
Programa para cargar y mostrar un diccionario de datos de empleados
Autor: Logica 01D
Fecha: Mayo-2024
Liciencia: GNU GPLV3
"""

from apoyo import mostrar_mensaje,ingresar_texto,convertir_empleado_mensaje,ingresar_empleado



def main():
	empleados=cargar_datos()
	mensaje=convertir_empleados_dic_mensaje(empleados)
	mostrar_mensaje(mensaje)
	
	
	
def cargar_datos():
	empleados={
	"3021":("3021","Diana","Jaramillo",23,1700000),\
	"4056":("4056","Luisa","Giraldo",28,3200000),\
	"5039":("5039","Ana","Montes",34,4500000),\
	"6712":("6712","Sofia","Tamayo",25,2300000),\
	"8001":("8001","Carolina","Rivera",39,5200000)\
	}
	return empleados

def leer_empleados_dic(mensaje_global,mensaje_empleado):
	mostrar_mensaje(mensaje_global)
	empleados=dict()
	numero_empleado=1
	mas_empleados="s"

	while mas_empleados=="s":
		empleado=ingresar_empleado(f"{mensaje_empleado} N° {numero_empleado}: ")
		
		codigo=empleado[0]
		empleados[codigo]=empleado
		numero_empleado+=1
		mas_empleados=ingresar_texto("más empleados(s/n):")

	return empleados

def convertir_empleados_dic_mensaje(empleados):

	mensaje=" "
	for codigo_empleado in empleados.keys():
		empleado=empleados[codigo_empleado]
		mensaje+=convertir_empleado_mensaje(empleado)
	return mensaje

		

main()