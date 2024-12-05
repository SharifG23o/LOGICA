from apoyo import ingresar_texto, mostrar_mensaje

def main():
    frase = ingresar_texto("Ingrese la frase: ")
    palindromo = invertir_frase(frase)
    mensaje = mensaje_palindromo(palindromo, frase)
    mostrar_mensaje(mensaje)

def invertir_frase(frase):
    frase_limpia = frase.lower().replace(" ", "")
    palindromo = frase_limpia[::-1]
    return palindromo

def mensaje_palindromo(palindromo, frase):
    if frase== invertir_frase(frase):
        mensaje = f"La frase '{frase}' es un palíndromo porque su palíndromo es {palindromo}"
    else:
        mensaje = f"La frase '{frase}' no es un palíndromo porque queda {palindromo}"
    return mensaje

main()
