""""
Programa para determinar el aumento en el recibo del agua
Autor: Area de programacion UQ
Fecha: Febrero 2024
Licencia: GNU GPL v3
"""


VALOR_METRO_CUBICO= 4500

def main():
    metros_consumidos= ingresar_entero("ingresar los metros cubicos consumidos")
    calcular_porcentaje_aumento= calcular_aumento(metros_consumidos, VALOR_METRO_CUBICO)
    calcular_valor_recibo= valor_recibo(metros_consumidos,calcular_porcentaje_aumento)
    mensaje= generar_mensaje(metros_consumidos, calcular_porcentaje_aumento, calcular_valor_recibo)
    mostrar_mensaje(mensaje)

def ingresar_entero(mensaje):
    entero= int(input(mensaje))
    return entero


def calcular_aumento(metros_consumidos, VALOR_METRO_CUBICO): 
    calcular_porcentaje_aumento= valor_recibo*calcular_aumento
    return calcular_porcentaje_aumento



def valor_recibo(metros_consumidos, calcular_porcentaje_aumento):
    calcular_valor_recibo= metros_consumidos*VALOR_METRO_CUBICO
    return calcular_porcentaje_aumento

def valor_final(metros_consumidos, calcular_porcentaje_aumento ):
    calcular_valor_final= valor_recibo+ valor_aumento 



def generar_mensaje(metros_consumidos, calcular_porcentaje_aumento, calcular_valor_recibo):








def determinar_porcentaje_aumento(consumo):

    if consumo>= 1 and consumo<=9:
        porcentaje_aumento= 0.15

    else:
        if consumo>=13 and consumo<= 15:
            porcentaje_aumento= 0.15 

        else: 
            if consumo>=20 and consumo<=28: 
                porcentaje_aumento=0.25 

            else: 
                porcentaje_aumento= 0.03 

    return porcentaje_aumento


