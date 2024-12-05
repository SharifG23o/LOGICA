"""
Programa que permite leer e imprimir los datos de un empleado, además de verificar si hay más
Autor: Programación UQ
Fecha:Mayo 2024
Licencia: GNU GPL v3

"""

from apoyo import ingresar_texto,mostrar_mensaje,ingresar_empleado, convertir_empleado_mensaje

def main():
    empleados=ingresar_empleados("Datos Empleados", "Ing.empleado")
    mensaje=convertir_empleados_mensaje(empleados)
    mostrar_mensaje(mensaje)


def ingresar_empleados(mensaje_global,mensaje):
    mostrar_mensaje(mensaje_global)#el mismo titulo para que salga en la pantalla
    numero_empleado=1
    empleados=[]
    respuesta="si"
    while respuesta=="si":
    
        empleado=ingresar_empleado(f"\n{mensaje} N° {numero_empleado+1}:")
        empleados.append(empleado)
        numero_empleado+=1
        respuesta=ingresar_texto("Más empleados(si/no): ")
    return empleados



def convertir_empleados_mensaje(empleados):

    mensaje=""
    for empleado in empleados:
        mensaje+=convertir_empleado_mensaje(empleado)

    return mensaje







main()