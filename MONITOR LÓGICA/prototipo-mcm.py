"""
Programa que permite hallar el MCM de 2 números
Autor:Programación UQ
Fecha:Abril 2024
Licencia:GNU GPL v3
"""


from apoyo import ingresar_entero_mayor_que, mostrar_mensaje

VALOR_MINIMO=0


def main():
    numero1=ingresar_entero_mayor_que("Ingrese el primer número: ", VALOR_MINIMO)
    numero2=ingresar_entero_mayor_que("Ingrese el segundo número: ")
    valor_mcm=calcular_mcm(numero1,numero2)
    mensaje=generar_mensaje_mcm(numero1,numero2, valor_mcm)
    mostrar_mensaje(mensaje)


def calcular_mcm(numero1,numero2):
    mcm=" "
    for mcm in (numero1,numero2+1):
        if verificar_es_divisible:
            mcm=mcm+1
            return mcm 
        
def verificar_es_divisible(numero1,numero2):
    es_divisible=numero1 or numero2//2==0 or numero1 or numero2//3 ==0 or numero1 or numero2//5 and 10==0
    return  es_divisible

def generar_mensaje_mcm(numero1,numero2, valor_mcm):
    mensaje= f"Con el valor del primer número {numero1} y el valor del segundo número {numero2}, el MCM ES: {valor_mcm}"
    return mensaje

main()
        