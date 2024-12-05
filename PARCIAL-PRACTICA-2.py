"""
programa que calcula el costo total de un viaje según la distancia recorrida y el medio de tranporte utilizado 
Autor: Programacion UQ
Fecha: Marzo 2024 
Licencia: GNU GPL v3 
"""
from apoyo import ingresar_texto, ingresar_real, mostrar_mensaje


def main(): 
    distancia=ingresar_real("Ingrese la distancia recorrida en KM: ")
    medio_de_transporte=ingresar_texto("Ingrese el medio de transporte utilizado: ")
    costo_km=calcular_costo_km(medio_de_transporte)
    costo_final=calcular_costo_final(distancia,costo_km)
    mensaje=generar_mensaje_final(distancia,medio_de_transporte,costo_final)
    mostrar_mensaje(mensaje)


def calcular_costo_km(medio_de_transporte):
    if medio_de_transporte=="tren":
        costo_km=2000
    else:
        
        costo_km=5000
    return costo_km

def calcular_costo_final(distancia,costo_km):
    costo_final= distancia*costo_km
    return costo_final

def generar_mensaje_final(distancia, medio_de_transporte,costo_final):
    mensaje= f"Con una distancia recorrida de {distancia} km y {medio_de_transporte} utilizado como medio de transporte,tiene un costo final a pagar de {costo_final} "
    return mensaje

main()