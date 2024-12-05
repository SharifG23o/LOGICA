from apoyo import convertir_empleado_mensaje, mostrar_mensaje

def main():
    empleados = cargar_datos_empleados()
    empleados_menores = empleados_menores_que(empleados)
    promedio_salarios = salario_empleados_mayores(empleados)
    mensaje = generar_mensaje_empleados(empleados, empleados_menores, promedio_salarios)
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
    lista_menores = []
    for empleado in empleados:
        if int(empleado[3]) < 30:
            lista_menores.append(empleado)
    return lista_menores

def salario_empleados_mayores(empleados):
    salarios_mayores = []
    for empleado in empleados:
        if int(empleado[3]) > 30:
            salarios_mayores.append(int(empleado[4]))
    if len(salarios_mayores) > 0:
        promedio = sum(salarios_mayores) / len(salarios_mayores)
    else:
        promedio = 0
    return promedio

def generar_mensaje_empleados(empleados, empleados_menores, promedio_salarios):
    mensaje = []
    mensaje.append(f"De los empleados {empleados}")
    mensaje.append(f"Los empleados menores de 30 son: {empleados_menores}")
    mensaje.append(f"Y los empleados mayores de 30, más el promedio de sus salarios son: {promedio_salarios}")
    return mensaje

main()
