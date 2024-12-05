"""
Programa para cargar y mostrar un conjunto de datos de varios empleados
Autor: Programación uUQ
Fecha: Mayo 2024
Licenca: GNU GPL V3
"""

from apoyo import convertir_empleado_mensaje, mostrar_mensaje

def main():
    empleados = cargar_datos_empleados()
    empleados_menores=empleados_menores_que(empleados)
    promedio_salarios=salario_empleados_mayores(empleados)
    mensaje = convertir_empleado_mensaje(empleados)
    mostrar_mensaje(mensaje)

def cargar_datos_empleados():
    empleados = [
        ("3021", "Diana", "Jaramillo", "23", "1700000"),
        ("4056", "Luisa", "Giraldo", "28", "3200000"),
        ("5039", "Ana", "Montes", "34", "4500000"),
        ("6712", "Sofia", "Tamayo", "25", "2300000"),
        ("8001", "Carolina", "Rivera", "39", "5200000")
    ]

    return empleados

def empleados_menores_que(empleados):
    
    lista_menores=[]
    for i in range (0,len(empleados)):
        if lista_menores[i]<30:
            lista_menores+=[i]
    return lista_menores

def salario_empleados_mayores(empleados):
    empleados_mayores=[]
    for i in range(0,len(empleados)):
        if empleados[i]>30:
            empleados_mayores+=[i]
    return empleados_mayores

main()
