from apoyo import ingresar_empleado, ingresar_entero, mostrar_mensaje, convertir_empleado_mensaje

def main():
    numero_empleados = ingresar_entero("Ingrese la cantidad de empleados: ")
    empleados = ingresar_empleados("INFORMACIÓN EMPLEADOS", "ING.EMPLEADO", numero_empleados)
    buscar_empleado(empleados)

def ingresar_empleados(mensaje_global, mensaje, numero_empleados):
    mostrar_mensaje(mensaje_global)  # El mismo título para mostrar en pantalla
    empleados = []
    for numero_empleado in range(0, numero_empleados):
        empleado = ingresar_empleado(f"\n{mensaje} N° {numero_empleado+1}:")
        empleados.append(empleado)
    return empleados

def buscar_empleado(empleados):
    buscado = ingresar_entero("Ingrese el ID del empleado a buscar: ")
    empleado_encontrado = "No se encontró ningún empleado con ese ID."
    encontrado = False
    for empleado in empleados:
        if empleado["ID"] == buscado:  # Comparar el ID del empleado
            empleado_encontrado = convertir_empleado_mensaje(empleado)
            encontrado = True
    if encontrado:
        mostrar_mensaje(f"Empleado encontrado:\n{empleado_encontrado}")
    else:
        mostrar_mensaje(empleado_encontrado)

main()
