
from apoyo import ingresar_entero_mayor_que, mostrar_mensaje

VALOR_MINIMO = 0

def main():
    numero1 = ingresar_entero_mayor_que("Ingrese el primer número: ", VALOR_MINIMO)
    numero2 = ingresar_entero_mayor_que("Ingrese el segundo número: ", VALOR_MINIMO)
    valor_mcm = calcular_mcm(numero1, numero2)
    mensaje = generar_mensaje_mcm(numero1, numero2, valor_mcm)
    mostrar_mensaje(mensaje)

def calcular_mcm(numero1, numero2):
    
    mcd = calcular_mcd(numero1, numero2)
    mcm = (numero1 * numero2) // mcd
    return mcm

def calcular_mcd(a, b):
    
    while b != 0:
        a, b = b, a % b
    return a

def generar_mensaje_mcm(numero1, numero2, valor_mcm):
    mensaje = f"Con el valor del primer número {numero1} y el valor del segundo número {numero2}, el MCM ES: {valor_mcm}"
    return mensaje

main()
