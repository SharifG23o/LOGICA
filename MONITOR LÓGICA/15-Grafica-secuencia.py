from apoyo import mostrar_mensaje, ingresar_entero_mayor_que

VALOR_MINIMO = 1

def main():
    numero = ingresar_entero_mayor_que("Ingrese el entero: ", VALOR_MINIMO)
    secuencia = obtener_secuencia_ULAM(numero)
    espacios = contar_espacios_secuencia(secuencia)
    area = calcular_area(espacios)
    grafica = mostrar_grafica(secuencia, espacios)
    mensaje = generar_mensaje_secuencia(numero, secuencia)
    mostrar_mensaje(mensaje)
    mostrar_mensaje(grafica)

def obtener_secuencia_ULAM(numero):
    secuencia = f"{numero}"
    while numero != 1:
        if numero % 2 == 0:
            numero = numero//2
        else:
            numero = numero*3+1
        secuencia += f" {numero}"
    return secuencia

def contar_espacios_secuencia(secuencia):
    espacios = 0 
    for i in secuencia:
        if i == " ":
            espacios += 1
    return espacios

def calcular_area(espacios):
    area = espacios * espacios // 2
    return area

def mostrar_grafica(secuencia, espacios):
    grafica = ""
    for i in range(1, espacios + 1):
        grafica += "*" * i + "\n"
    return grafica

def generar_mensaje_secuencia(numero, secuencia):
    mensaje = f"Con el número siendo {numero}, la secuencia es {secuencia}"
    return mensaje

main()
