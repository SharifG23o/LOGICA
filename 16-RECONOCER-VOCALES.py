from apoyo import ingresar_texto, mostrar_mensaje

def main():
    oracion = ingresar_texto("Ingrese la oración: ")
    oracion_minuscula = convertir_a_minuscula(oracion)
    vocales_capitalizadas = convertir_vocales(oracion_minuscula)
    mensaje = mensaje_oracion(oracion, oracion_minuscula, vocales_capitalizadas)
    mostrar_mensaje(mensaje)

def convertir_a_minuscula(oracion):
    oracion_minusculas = ""
    for letra in oracion:
        oracion_minusculas += letra.lower()
    return oracion_minusculas

def convertir_vocales(oracion_minuscula):
    vocales_mayuscula = ""
    for letra in oracion_minuscula:
        if letra in "aeiouAEIOU":
            vocales_mayuscula += letra.upper()
        else:
            vocales_mayuscula += letra
    return vocales_mayuscula

def mensaje_oracion(oracion, oracion_minuscula, vocales_capitalizadas):
    mensaje = f"La oración ingresada es '{oracion}', en minúscula '{oracion_minuscula}' y sus vocales en mayúsculas son '{vocales_capitalizadas}'."
    return mensaje

main()
