"""
Programa que permite leer e imprimir los datos de varios empleados
autor:prog. uq
fecha:mayo 2024
licencia: GNU GPL v3
"""


from apoyo import ingresar_empleado,ingresar_entero,mostrar_mensaje, convertir_empleado_mensaje

def main():
    numero_empleados=ingresar_entero("Ingrese la cantidad de empleados: ") 
    #no se recomiendo ponerle a la variable el nombre de la estructura por reutilización ej: lista_empleados(no), solo empleados
    empleados=ingresar_empleados("INFORMACIÓN EMPLEADOS", "ING.EMPLEADO",numero_empleados)
    mensaje=convertir_empleados_mensaje(empleados)
    mostrar_mensaje(mensaje)

def ingresar_empleados(mensaje_global,mensaje,numero_empleados):
    mostrar_mensaje(mensaje_global)#el mismo titulo para que salga en la pantalla
    empleados=[]
    for numero_empleado in range(0,numero_empleados):
        empleado=ingresar_empleado(f"\n{mensaje} N° {numero_empleado+1}:")
        empleados.append(empleado)
    return empleados

def convertir_empleados_mensaje(empleados):

    mensaje=""
    for empleado in empleados:
        mensaje+=convertir_empleado_mensaje(empleado)
    return mensaje



main()
