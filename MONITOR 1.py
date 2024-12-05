"""
programa que permite calcular el factorial de un numero
autor: prog. UQ 
fecha: agosto 2024
licencia: GNU GPL v3 

"""


def main(): 
    numero=ingresar_entero("Ingrese el número: ")
    factorial=calcular_factorial(numero)
    mensaje=generar_mensaje_factorial(numero,  factorial)
    mostrar_mensaje(mensaje)

def calcular_factorial(numero):
      factorial=1
      for i in range (1,numero+1): 
            factorial *=i
      return factorial
    
def generar_mensaje_factorial(numero, factorial): 
     mensaje= f"El factorial de {numero} es {factorial}"
     return mensaje

def ingresar_entero(mensaje):
     entero=int(input(mensaje))
     return entero

def mostrar_mensaje(mensaje):
     print(mensaje)

main()