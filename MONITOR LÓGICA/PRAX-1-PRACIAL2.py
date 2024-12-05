"""
Programa que dado un numero n positivo imprima una secuencia triangular con base y altura los números
Autor:Pprogramacion UQ 
Fecha: Abril 2024
Licencia: GNU GPL v3

"""


from apoyo import mostrar_mensaje, ingresar_entero_rango


VALOR_MINIMO=1
VALOR_MAXIMO=10


def main():
    numero = ingresar_entero_rango("Ingrese un número entero: ", VALOR_MINIMO,VALOR_MAXIMO)
    secuencia = generar_grafica(numero)
    mostrar_mensaje(secuencia)


def generar_grafica(numero):
    grafica = ""
    for i in range(1, numero + 1):
        grafica += f"{i}"*i
        grafica+="\n"
    return grafica

main()
