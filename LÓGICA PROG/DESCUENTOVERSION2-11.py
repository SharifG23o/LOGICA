""""
Programa para determinar el descuento según día de nacimiento y género 
Autor: Area de programacion UQ
Fecha: Febrero 2024
Licencia: GNU GPL v3
"""    
     

from apoyo import ingresar_texto, ingresar_real, ingresar_entero, mostrar_mensaje 

def main():
    genero = ingresar_texto("Ingrese su género:").lower()
    dia_nacimiento = ingresar_entero("Ingrese su día de nacimiento: ")
    valor_cuenta = ingresar_real("Ingrese el valor de su cuenta")
    
    porcentaje_descuento = determinar_porcentaje_descuento(genero, dia_nacimiento)
    valor_final = determinar_valor_final(valor_cuenta, porcentaje_descuento)
    mensaje_descuento = generar_mensaje_descuento(genero, dia_nacimiento, valor_cuenta, porcentaje_descuento, valor_final)
    mostrar_mensaje(mensaje_descuento)

def determinar_porcentaje_descuento(genero, dia_nacimiento):
    if genero == "mujer":
        if dia_nacimiento % 2 == 0: 
            return 0.10  # Descuento del 12% para mujeres nacidas en día par
        else: 
            return 0.07  # Descuento del 8% para mujeres nacidas en día impar
    elif genero == "hombre":
        if 3 <= dia_nacimiento <= 14 or 17 <= dia_nacimiento <= 21:
            return 0.10  # Descuento del 10% para hombres nacidos en ciertos días
        elif 1 <= dia_nacimiento <= 2:
            return 0.07  # Descuento del 7% para hombres nacidos en ciertos días
        elif 15 <= dia_nacimiento <= 16:
            return 0.09  # Descuento del 9% para hombres nacidos en ciertos días
        else: 
            return 0.03  # Descuento del 3% para hombres nacidos en otros días

def determinar_valor_final(cuenta, descuento):
     
     return cuenta - (cuenta * descuento)

def generar_mensaje_descuento(genero, dia_nacimiento, valor_cuenta, descuento, valor_final):
     mensaje = f"Con su género {genero}, su fecha de nacimiento {dia_nacimiento} y el valor de su cuenta {valor_cuenta}, su descuento aplicado es de {descuento*100:.2f}%, y su valor final a pagar es de {valor_final:.2f}"
     return mensaje

main()