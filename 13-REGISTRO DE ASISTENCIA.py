"""
programa que permite genrar un listado 
autor: prog. UQ 
fech: abril 2024
licencia: GNU GPL v3 

"""

from apoyo import ingresar_entero_mayor_que, mostrar_mensaje

VALOR_INICIAL = 0


def main():
    valor_inicial = ingresar_entero_mayor_que(
        "Ingrese el valor inicial: ", VALOR_INICIAL)
    valor_final = ingresar_entero_mayor_que(
        "Ingrese el valor final: ", valor_inicial)
    listado = generar_listado(valor_inicial, valor_final)
    mostrar_mensaje(listado)


def generar_listado2(valor_inicial, valor_final):
    listado = ""
    i = valor_inicial
    while i <= valor_final:
        listado += f"{i:3d}.______________________________________\n."
        i = i+1
    return listado

# for (i=valor_inicial; i<=valor_final; i+=1)


def generar_listado(valor_inicial, valor_final):
    listado = ""
    for i in range(valor_inicial, valor_final+1, 2):
        listado += f"{i:3d}.______________________________________\n."
    return listado


main()
