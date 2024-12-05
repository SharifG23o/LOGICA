from apoyo import convertir_empleado_mensaje, mostrar_mensaje

def main():
    empleados = cargar_datos_empleados()
    empleados_menores, contador_menores = empleados_menores_y_contador(empleados)
    total_salarios_mayores, contador_mayores = salario_empleados_mayores_y_total(empleados)
    promedio_salarios = 0
    if contador_mayores > 0:
        promedio_salarios = total_salarios_mayores / contador_mayores
    mensaje = generar_mensaje_empleados(empleados, empleados_menores, contador_menores, promedio_salarios)
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

def empleados_menores_y_contador(empleados):
    lista_menores = []
    contador_menores = 0
    for empleado in empleados:
        if int(empleado[3]) < 30:
            lista_menores.append(empleado)
            contador_menores += 1
    return lista_menores, contador_menores

def salario_empleados_mayores_y_total(empleados):
    total_salarios_mayores = 0
    contador_mayores = 0
    for empleado in empleados:
        if int(empleado[3]) > 30:
            total_salarios_mayores += int(empleado[4])
            contador_mayores += 1
    return total_salarios_mayores, contador_mayores

def generar_mensaje_empleados(empleados, empleados_menores, contador_menores, promedio_salarios):
    mensaje = (f"De los empleados {empleados}""\n"
               f"Los empleados menores de 30 son: {empleados_menores}""\n"
               f"El número de empleados menores de 30 es: {contador_menores}""\n"
               f"Y los empleados mayores de 30, más el promedio de sus salarios son: {promedio_salarios}")
    return mensaje

main()
