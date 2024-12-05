"""
Programa que muestra la cantidad de destellos de luz emitida por un faro en determinada cantidad de tiempo
Autor: Programacion UQ 
Fecha:Marzo 2024
Licencia: GNU GPL v3
"""
from apoyo import ingresar_entero, mostrar_mensaje

HORA= 60

def main():
    destellos_por_minuto=ingresar_entero("Ingrese la cantidad de destellos por minuto del faro: ")
    horas_funcionamiento=ingresar_entero("Ingrese las horas de funcionamiento del faro: ")
    minutos_funcionamiento=ingresar_entero("Ingrese los minutos de funcionamiento: ")
    destellos_totales=calcular_total_destellos(destellos_por_minuto,horas_funcionamiento,minutos_funcionamiento)
    mensaje=mensaje_final_destellos(destellos_por_minuto,destellos_totales,horas_funcionamiento,minutos_funcionamiento)
    mostrar_mensaje(mensaje)

def calcular_total_destellos(destellos_por_minuto,horas_funcionamiento,minutos_funcionamiento):
    destellos_totales= destellos_por_minuto*horas_funcionamiento*60+minutos_funcionamiento
    return destellos_totales

def mensaje_final_destellos(destellos_por_minuto, destellos_totales,horas_funcionamiento,minutos_funcionamiento):
    mensaje=f"Apreciado público, El planetario informa que el faro produce {destellos_totales} destellos para {horas_funcionamiento} horas  y {minutos_funcionamiento} minutos, teniendo en cuenta que son {destellos_por_minuto} destellos por minuto"
    return mensaje

main()