""""
Modulo de funciones
Autor: Area de programacion UQ
Fecha: Febrero 2024
Licencia: GNU GPL v3
"""


def ingresar_entero_mayor_que(mensaje, valor_minimo):
    repetir = True
    while repetir:
        valor = ingresar_entero(mensaje)
        if valor > valor_minimo:
            repetir = False
        else:
            print(f"El valor no es mayor que {valor_minimo}")

    return valor




def ingresar_texto(mensaje):
    texto = input(mensaje)
    return texto


def ingresar_entero(mensaje):
    repetir = True
    while repetir:
        try:
            entero = int(input(mensaje))
            repetir = False
        except:
            print("Error, no ingresó un entero")
    return entero


def ingresar_real(mensaje):
    repetir = True
    while repetir:
        try:
            real = float(input(mensaje))
            repetir = False
        except:
            print("Error, no ingresó un real")
    return real


def mostrar_mensaje(mensaje):
    print(mensaje)


def calcular_promedio(valor1, valor2, valor3, valor4, valor5):
    promedio = (valor1 + valor2 + valor3 + valor4 + valor5) / 5
    return promedio


def ingresar_real_rango(mensaje, valor_minimo, valor_maximo):
    repetir = True
    while repetir:
        valor = ingresar_real(mensaje)
        if valor < valor_minimo or valor > valor_maximo:
            print(f"El valor no está entre {valor_minimo} y {valor_maximo}")
        else:
            repetir = False
    return valor


def ingresar_entero_rango(mensaje, valor_minimo, valor_maximo):
    repetir = True
    while repetir:
        valor = ingresar_entero(mensaje)
        if valor < valor_minimo or valor > valor_maximo:
            print(f"El valor no está entre {valor_minimo} y {valor_maximo}")
        else:
            repetir = False
    return valor


def generar_listado2(valor_inicial, valor_final):
    listado = ""
    i = valor_inicial
    while i <= valor_final:
        listado += f"{i:3d}.______________________________________\n."
        i = i+1
    return listado


def generar_listado(valor_inicial, valor_final):
    listado = ""
    for i in range(valor_inicial, valor_final):
        listado += f"{i:3d}.______________________________________\n."
    return listado


def generar_mensaje_tabla_multiplicar(numero_tabla, minimo_valor, maximo_valor):
    mensaje_tabla = f"\n  TABLA DE MULTIPLICAR DEL {numero_tabla}\n\n "
    i = minimo_valor
    while i <= maximo_valor:
        producto = numero_tabla*i
        mensaje_tabla += f"{numero_tabla:2d}x{i:2d}={producto:3d}\n"
        i += 1
    return mensaje_tabla


def generar_mensaje_tabla_multiplicar2(numero_tabla, minimo_valor, maximo_valor):
    mensaje_tabla = f"\n  TABLA DE MULTIPLICAR DEL {numero_tabla}\n\n "
    
    for i in range (minimo_valor, maximo_valor+1):
        producto = numero_tabla*i
        mensaje_tabla += f"{numero_tabla:2d}x{i:2d}={producto:3d}\n"
        i += 1
    return mensaje_tabla