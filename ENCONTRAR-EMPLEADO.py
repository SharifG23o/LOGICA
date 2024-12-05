from apoyo import ingresar_texto, mostrar_mensaje, convertir_empleado_mensaje

# Base de datos de empleados (simulada)
empleados = {
    "001": {"nombre": "Juan", "apellido": "Perez", "edad": 30, "sueldo": 30000},
    "002": {"nombre": "Maria", "apellido": "Gomez", "edad": 25, "sueldo": 35000},
    "003": {"nombre": "Luis", "apellido": "Gonzalez", "edad": 35, "sueldo": 28000}
}

def main():
    codigo_empleado = ingresar_texto("Ingrese el código del empleado: ")
    empleado = buscar_empleado_por_codigo(codigo_empleado)
    if empleado:
        mensaje = convertir_empleado_mensaje(empleado)
        mostrar_mensaje(mensaje)
    else:
        mostrar_mensaje("No se encontró ningún empleado con ese código.")

def buscar_empleado_por_codigo(codigo):
    empleado = empleados.get(codigo)
    return empleado

def convertir_empleado_mensaje(empleado):
    codigo_empleado = empleado
    nombre = empleado["nombre"]
    apellido = empleado["apellido"]
    edad = empleado["edad"]
    sueldo = empleado["sueldo"]

    mensaje = f"{codigo_empleado}: {nombre} {apellido}, con {edad} años, gana {sueldo}.\n"
    return mensaje

main()
