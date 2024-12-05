""""
Programa 
Autor: Area de programacion UQ
Fecha: Febrero 2024
Licencia: GNU GPL v3
"""    
from apoyo import ingresar_real, ingresar_texto, mostrar_mensaje

def main():
    medio_transporte = ingresar_texto("Ingrese el medio de transporte utilizado: ")
    distancia_recorrida = ingresar_real("Ingrese la distancia recorrida en km: ")
    costo_km = costo_por_distancia(medio_transporte)
    costos_medios = costo_por_medio(medio_transporte, distancia_recorrida)
    costo_final = valor_final(distancia_recorrida, costos_medios)
    mensaje = generar_mensaje(medio_transporte, distancia_recorrida, costo_final)
    mostrar_mensaje(mensaje)

def costo_por_medio(medio_transporte, distancia_recorrida):
    if medio_transporte == "tren":
        costo_por_medio = 2000
    else:
        costo_por_medio = 5000
    return costo_por_medio

def costo_por_distancia(medio_transporte):
    if medio_transporte == "tren":
        costo_por_distancia = 2000
    else:
        costo_por_distancia = 5000
    return costo_por_distancia

def valor_final(distancia_recorrida, costo_km):
    costo_final = distancia_recorrida * costo_km
    return costo_final

def generar_mensaje(medio_transporte, distancia_recorrida, costo_final):
    mensaje = f"Con {medio_transporte} como medio de transporte utilizado y una distancia recorrida de {distancia_recorrida} km tiene un costo final de ${costo_final}"
    return mensaje
    
main()
