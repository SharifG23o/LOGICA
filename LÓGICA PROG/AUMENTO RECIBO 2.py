""""
Programa para determinar el porcentaje de aumento en el recibo del agua
Autor: Area de programacion UQ
Fecha: Febrero 2024
Licencia: GNU GPL v3
"""


def main():
    valor_recibo = ingresar_entero("Ingrese el valor del metro cúbico:")
    consumidos = ingresar_entero("Ingrese los metros consumidos:")
    porcentaje_aumento = determinar_porcentaje_aumento(consumidos)
    valor_final = calcular_valor_final(valor_recibo, porcentaje_aumento)
    mensaje_aumento = generar_mensaje_aumento(consumidos, porcentaje_aumento, valor_final)
    mostrar_mensaje(mensaje_aumento)

def ingresar_entero(mensaje):
    return int(input(mensaje))

def determinar_porcentaje_aumento(consumo):
    if consumo >= 1 and consumo <= 9:
        return 0.15
    elif consumo >= 13 and consumo <= 15:
        return 0.15
    elif consumo >= 20 and consumo <= 28:
        return 0.25
    else:
        return 0.03

def valor_recibo(consumo, valor_metros):
    return consumo * valor_metros

def calcular_valor_final(recibo, aumento):
    return recibo + aumento

def generar_mensaje_aumento(consumidos, porcentaje_aumento, valor_final):
    mensaje = (f"Con {consumidos} metros cúbicos consumidos, obtiene un aumento de "
               f"{porcentaje_aumento} y su valor final es de {valor_final}")
    return mensaje

def mostrar_mensaje(mensaje):
    print(mensaje)

main()