""""
Programa para determinar si con la temperatura el agua hierve o no 
Autor: Area de programacion UQ
Fecha: Febrero 2024
Licencia: GNU GPL v3
"""
from apoyo import ingresar_real, mostrar_mensaje

def main():
    valor_temperatura=ingresar_real("Ingrese el valor de la temperatura en grados Celcius °C: ")
    mensaje= generar_mensaje_final(valor_temperatura,)
    mostrar_mensaje(mensaje)
    

def generar_mensaje_final(valor_temperatura):
    if valor_temperatura>= 100:
        mensaje= f"Con una temperatura de {valor_temperatura} °C, el agua puede hervir"

    else:
        mensaje= f"Con una temperatura de {valor_temperatura} °C el agua no puede hervir"

    return mensaje

main()