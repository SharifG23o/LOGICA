""""
Programa para determinar el descuento según día de nacimiento y género 
Autor: Area de programacion UQ
Fecha: Febrero 2024
Licencia: GNU GPL v3
"""    

HORA=60
from apoyo import ingresar_entero, mostrar_mensaje

def main(): 
    destellos_por_minuto=ingresar_entero("Ingrese la cantidad de destellos registrados por minuto: ")
    horas=ingresar_entero("Ingrese la cantidad de horas que ha funcionado el faro: ")
    minutos=ingresar_entero("Ingrese la cantdad de minutos que ha funcionado el faro")
    tiempo=calcular_tiempo_minutos(horas,minutos)
    detellos=calcular_destellos_faro(tiempo,destellos_por_minuto)
    mensaje= generar_mensaje(destellos_por_minuto,horas,minutos,detellos)
    mostrar_mensaje(mensaje)

def calcular_tiempo_minutos(horas,minutos):
    tiempo= HORA*horas+minutos
    return tiempo

def calcular_destellos_faro(tiempo, destellos_por_minuto):
    destellos=tiempo*destellos_por_minuto
    return destellos

def generar_mensaje(destellos_por_minuto,horas,minutos,destellos ):
    mensaje= f"Apreciado público, el planetario le informa que el faro produce {destellos} destellos para {horas} horas y { minutos} minutos, teniendo en cuenta que son {destellos_por_minuto} destellos por minuto"
    return mensaje


main()
