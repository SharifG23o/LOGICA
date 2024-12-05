""""
Programa para determinar el descuento según día de nacimiento y género 
Autor: Area de programacion UQ
Fecha: Febrero 2024
Licencia: GNU GPL v3
"""   
from apoyo import ingresar_entero, ingresar_real, mostrar_mensaje

def main():
    ingresar_edad= ingresar_entero("Ingrese su edad: ")
    promedio_edad= calcular_promedio_edad(ingresar_edad)
    categoria_peso= determinar_categoria_peso(promedio_edad)
    mensaje= generar_mensaje(promedio_edad,categoria_peso)