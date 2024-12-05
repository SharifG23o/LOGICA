""""
Programa para determinar cuantas cajas completas de fruta fresca se necesitan para trasladar un pedido
Autor: Area de programacion UQ
Fecha: Febrero 2024
Licencia: GNU GPL v3
"""

def main():
    a= ingresar_entero("Ingrese valor a:")
    b= ingresar_entero("Ingrese valor b:")
    c= ingresar_entero("Ingrese valor c:")
    d= ingresar_entero("Ingrese valor d:")
    e= ingresar_entero("Ingrese valor e:")

    mayor= obtener_mayor5(a,b,c,d,e)
    mensaje= generar_mensaje(mayor)
    mostrar_mensaje(mensaje)


def ingresar_entero(mensaje):
    entero= int(input(mensaje))
    return entero

def obtener_mayor(a,b):
    if a>b:
        mayor=a 
    else:
        mayor=b 

    return mayor
    
def obtener_mayor5(a,b,c,d,e):
    mayor=obtener_mayor(a,b)
    mayor=obtener_mayor(mayor,c)
    mayor= obtener_mayor(mayor, d)
    mayor= obtener_mayor(mayor,e)
    return mayor

def generar_mensaje(mayor):
    mensaje= f"el valor mayor es {mayor}"
    return mensaje

def mostrar_mensaje(mensaje):
    print(mensaje)

main()


    