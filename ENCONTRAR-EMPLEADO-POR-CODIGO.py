"""
Programa que permite leer e imprimir los datos de varios empleados y encontrarolos por su código
autor:prog. uq
fecha:mayo 2024
licencia: GNU GPL v3
"""
from apoyo import ingresar_empleado, ingresar_entero, mostrar_mensaje, convertir_empleado_mensaje, ingresar_texto

def main():
    numero_empleados = ingresar_entero("Ingrese la cantidad de empleados: ")
    empleados = ingresar_empleados("INFORMACIÓN EMPLEADOS", "ING.EMPLEADO", numero_empleados)
    mensaje = convertir_empleados_mensaje(empleados)
    mostrar_mensaje(mensaje)

    buscar_codigo = ingresar_texto("Ingrese el código del empleado a buscar: ")
    empleado_encontrado = empleado_por_codigo(buscar_codigo, empleados)
    mostrar_mensaje(empleado_encontrado)

def ingresar_empleados(mensaje_global, mensaje, numero_empleados):
    mostrar_mensaje(mensaje_global)
    empleados = []
    for numero_empleado in range(0, numero_empleados):
        empleado = ingresar_empleado(f"\n{mensaje} N° {numero_empleado+1}: ")
        empleados.append(empleado)
    return empleados

def convertir_empleado_mensaje(empleado):
    return f"Código: {empleado['codigo']}, Nombre: {empleado['nombre']}, Edad: {empleado['edad']}, Salario: {empleado['salario']}\n"

def convertir_empleados_mensaje(empleados):
    mensaje = ""
    for empleado in empleados:
        mensaje += convertir_empleado_mensaje(empleado)
    return mensaje

def empleado_por_codigo(codigo, empleados):
    for empleado in empleados:
        if codigo == empleado['codigo']:
            return convertir_empleado_mensaje(empleado)
    return "No se ha encontrado ningún empleado que coincida con el código ingresado."

main()
