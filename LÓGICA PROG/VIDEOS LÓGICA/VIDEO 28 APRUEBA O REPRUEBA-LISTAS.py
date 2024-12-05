
from apoyo import ingresar_entero_mayor_que, ingresar_real_rango, ingresar_texto, mostrar_mensaje

CANTIDAD_MINIMA=0
NOTA_MINIMA=0.0
NOTA_MAXIMA=5.0


def main():
    cantidad_estudiantes = ingresar_entero_mayor_que("Ingrese la cantidad de estudiantes: ", CANTIDAD_MINIMA)
    nota_minima_aprobar = ingresar_real_rango("Ingrese la nota mínima para aprobar: ", NOTA_MINIMA, NOTA_MAXIMA)
    nombres_estudiantes = ingresar_n_textos("Ingrese el nombre del estudiante", cantidad_estudiantes)
    notas_estudiantes = ingresar_n_real_rango("Ingrese la nota", cantidad_estudiantes, NOTA_MINIMA, NOTA_MAXIMA)
    estudiantes_aprobaron = obtener_estudiantes_aprobaron(nombres_estudiantes, notas_estudiantes, nota_minima_aprobar)
    estudiantes_reprobaron = obtener_estudiantes_reprobaron(nombres_estudiantes, notas_estudiantes, nota_minima_aprobar)
    mensaje_notas = generar_mensaje_notas(estudiantes_aprobaron, estudiantes_reprobaron)
    mostrar_mensaje(mensaje_notas)

def ingresar_n_textos(mensaje, cantidad):
    textos = [""] * cantidad
    for i in range(0, len(textos)):
        textos[i] = ingresar_texto(f"{mensaje} ({i+1} de {cantidad}): ")
    return textos

def ingresar_n_real_rango(mensaje, cantidad, valor_minimo, valor_maximo):
    valores = [0.0] * cantidad
    for i in range(0, len(valores)):
        valores[i] = ingresar_real_rango(f"{mensaje} ({i+1} de {cantidad}): ", valor_minimo, valor_maximo)
    return valores

def obtener_estudiantes_aprobaron(nombres, notas, nota_minima):
    estudiantes_aprobaron = []
    for i in range(0, len(notas)):
        if notas[i] >= nota_minima:
            estudiantes_aprobaron.append(nombres[i])
    return estudiantes_aprobaron

def obtener_estudiantes_reprobaron(nombres, notas, nota_minima):
    estudiantes_reprobaron = []
    for i in range(0, len(notas)):
        if notas[i] < nota_minima:
            estudiantes_reprobaron.append(nombres[i])
    return estudiantes_reprobaron

def generar_mensaje_notas(estudiantes_aprobaron, estudiantes_reprobaron):
    mensaje = (f"Los estudiantes que aprobaron son:\n"
               f"{obtener_elementos(estudiantes_aprobaron)}"
               f"y son en total {len(estudiantes_aprobaron)}\n\n"
               f"Los estudiantes que reprobaron son:\n"
               f"{obtener_elementos(estudiantes_reprobaron)}"
               f"y son en total {len(estudiantes_reprobaron)}\n\n"
              )
    return mensaje

def obtener_elementos(lista):
    mensaje = ""
    for elemento in lista:
        mensaje += f"{elemento}\n"
    return mensaje

main()
