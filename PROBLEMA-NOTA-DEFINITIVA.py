""""
Programa para determinar el mensaje dependiendo de la definitiva del estudiante
Autor: Area de programacion UQ
Fecha: Marzo 2024
Licencia: GNU GPL v3
"""

from apoyo import ingresar_real, mostrar_mensaje

def main():
    
    nota1= ingresar_real("Ingrese valor de la nota 1:")
    nota2= ingresar_real("Ingrese valor de la nota 2:")
    nota3= ingresar_real("Ingrese valor de la nota 3:")
    nota4= ingresar_real("Ingrese valor de la nota 4:")
    notas= nota_definitiva(nota1,nota2,nota3,nota4)
    mensaje=mensaje_nota_final(nota_definitiva)
    mostrar_mensaje(mensaje)

def nota_definitiva(nota1,nota2,nota3,nota4):
    nota_definitiva= 0.10*nota1+0.20*nota2+0.30*nota3+0.40*nota4
    return nota_definitiva

def mensaje_nota_final(nota_definitiva):
    if nota_definitiva<2.9: 
        mensaje="PODEMOS MEJORAR"
    elif  nota_definitiva<3.6:
        mensaje="YA ESTAMOS CERCA"
    elif nota_definitiva<4.7:
        mensaje="MUY BIEN"
    else:
        mensaje="EXCELENTE"
    return mensaje


main()