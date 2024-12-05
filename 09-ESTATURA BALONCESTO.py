""""
Programa para determinar la posición en un equipo de baloncesto según la estatura
Autor: Area de programacion UQ
Fecha: Febrero 2024
Licencia: GNU GPL v3
"""

def main():
    estatura = ingresar_real("Ingrese el valor de su estatura en metros: ")
    mensaje_posicion = generar_mensaje_posicion(estatura)
    mostrar_mensaje(mensaje_posicion)

def ingresar_real(mensaje):
    return float(input(mensaje))

def determinar_posicion(estatura):
    if estatura < 1.90:
        return "base"
    elif estatura >= 1.90 and estatura <= 2.00:
        return "escolta"
    elif estatura >= 2.00 and estatura <= 2.10:
        return "alero"
    elif estatura >= 2.10:
        return "ala pivot"

def generar_mensaje_posicion(estatura):
    posicion = determinar_posicion(estatura)
    mensaje = (f"Con {estatura: .2f} metros de estatura, su posición es de {posicion}.")
    return mensaje

def mostrar_mensaje(mensaje):
    print(mensaje)

main()
