"""
Programa para cargar y mostrar un diccionario de datos de empleados
Autor: Logica 01D
Fecha: Mayo-2024
Liciencia: GNU GPLV3
"""

from apoyo import mostrar_mensaje,ingresar_texto,convertir_empleado_mensaje



def main():
	empleados=cargar_datos_dic()
	mensaje=convertir_empleados_dic_mensaje(empleados)
	mostrar_mensaje(mensaje)
	
	

	
	
def cargar_datos_dic():
	
	empleados={
	"3021":{"codigo": "3021",
	"nombre": "Diana",
	"apellido": "Jaramillo",
	"edad":23,
	"salario":17000000
	},

	"4056":{"codigo": "4056",
	"nombre": "Luisa",
	"apellido": "Giraldo",
	"edad":28,
	"salario":3200000
	}
	}

	return empleados

def leer_empleados_dic(mensaje_global,mensaje_empleado):
	mostrar_mensaje(mensaje_global)
	empleados=dict()
	numero_empleado=1
	mas_empleados="s"

	while mas_empleados=="s":
		empleado=ingresar_empleado_dic(f"{mensaje_empleado} N° {numero_empleado}: ")
		
		codigo=empleado["codigo"]
		empleados[codigo]=empleado
		numero_empleado+=1
		mas_empleados=ingresar_texto("más empleados(s/n):")

	return empleados

def convertir_empleados_dic_mensaje(empleado):

	if empleado!=None:
		mensaje=(
			f"{empleado['codigo']}"
			f"{empleado['nombre']}"
			f"{empleado['apellido']}"
			f"{empleado['edad']}"
			f"{empleado['salario']}"
        )
	else:
		mensaje="No hay datos"
	return mensaje

def ingresar_empleado_dic(mensaje):
	mostrar_mensaje(mensaje)
	empleado= {
		
        "codigo":ingresar_texto("Ingrese el código: "),
		"nombre":ingresar_texto("Ingrese el nombre: "),
		"apellido":ingresar_texto("Ingrese el apellido: "),
		"edad":ingresar_texto("Ingrese la edad: "),
		"sueldo":ingresar_texto("Ingrese el sueldo: ")
    }
	return empleado


		


main()