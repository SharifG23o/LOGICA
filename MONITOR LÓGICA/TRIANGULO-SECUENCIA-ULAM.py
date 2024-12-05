"""
Programa que permite 
autor:programacion UQ 
fecha:abril 2024
licencia: GNU GPL v3 

"""



from apoyo import mostrar_mensaje, ingresar_entero_mayor_que

VALOR_MINIMO = 1

def main():
    numero = ingresar_entero_mayor_que("Ingrese el entero: ", VALOR_MINIMO)
    secuencia = obtener_secuencia_ULAM(numero)
    espacios = contar_espacios_secuencia(secuencia)
    area_triangulo = calcular_area(secuencia, espacios)
    grafica = mostrar_grafica(secuencia)
 
    mostrar_mensaje(grafica)


def obtener_secuencia_ULAM(numero):
    secuencia = f"{numero}"
    while numero != 1:
        if numero % 2 == 0:
            numero = numero // 2
        else:
            numero = numero * 3 + 1
        secuencia += f" {numero}"
    return secuencia

def contar_espacios_secuencia(secuencia):
   cantidad=0
   for c in secuencia:
       if c==" ":
           cantidad+=1
           return cantidad

def calcular_area(secuencia, espacios):
    return (espacios * (espacios + 1)) // 2

def mostrar_grafica(secuencia):
    espacios = contar_espacios_secuencia(secuencia)
    for i in range(1, espacios + 1):
        print("*" * i)

    


main()