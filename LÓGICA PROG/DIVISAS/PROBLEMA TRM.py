"""""
Programa que imprime el valor del TRM
Autor: Area de programacion UQ
Fecha: Febrero 2024
Licencia: GNU GPL v3
"""
def main(): 
    valor_trm= ingresar_entero("Ingresar el valor TRM:")
    mensaje= generar_mensaje_trm(valor_trm)
    mostrar_mensaje=mensaje

def ingresar_entero(mensaje):
    valor= int(input(mensaje))
    return valor


def generar_mensaje_trm(valor_trm):
    mensaje= f"El valor del TRM es{valor_trm}"
    return mensaje



def mostrar_mensaje(mensaje):
    print(mensaje)


main()