""""
Programa para sugerir skin a un jugador segun sus datos
Autor: Area de programacion UQ
Fecha: Febrero 2024
Licencia: GNU GPL v3
"""

from apoyo import ingresar_texto, ingresar_real, ingresar_entero, mostrar_mensaje 

def main():
    genero= ingresar_texto("Ingrese su genero:")
    pavos= ingresar_real("Ingrese su cantidad de miles de PaVos: ")
    temporada= ingresar_entero("Ingrese su temporada:")
    edad= ingresar_entero("Ingrese su edad:")
    sugerencia_skin= verificar_skin(genero,pavos,temporada,edad) 
    mensaje_sugerencia= generar_mensaje_sugerencia(sugerencia_skin)
    mostrar_mensaje(mensaje_sugerencia)

def verificar_skin(genero,pavos,temporada,edad):
    sugerencia_mujer= verificar_skin_mujer(genero,pavos,temporada,edad)
    sugerencia_hombre= verificar_skin_hombre(genero,pavos,temporada,edad)
    sugerencia_skin= sugerencia_mujer or sugerencia_hombre
    return sugerencia_skin

def verificar_skin_mujer(genero, pavos, temporada,edad):
    sugerencia_mujer=  genero== "mujer" and pavos== "2.6" and temporada>6 and edad >= 18 and edad <=25
    return sugerencia_mujer

def verificar_skin_hombre(genero, pavos, temporada, edad):
    ingresa_hombre=  genero== "hombre" and pavos== "4.9" and temporada>6 and edad >= 18 and edad <=24
    return ingresa_hombre

def generar_mensaje_sugerencia(sugerencia_skin):

    if verificar_skin_mujer:
        mensaje="la skin sugerida es Tarana" 
    if verificar_skin_hombre:
            mensaje= "La skin sugerida es Caballero tenebroso"
    
    else: 
        mensaje="sus datos no permiten generarle una skin"
    return mensaje

main()