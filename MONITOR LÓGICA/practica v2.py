



from apoyo import ingresar_entero, mostrar_mensaje

def main(): 
    lado = ingresar_entero("Ingrese la longitud del lado del cuadrado: ")
    figura = generar_figura(lado)
    mostrar_mensaje(figura)

def generar_figura(lado):
    figura = ""
    for i in range(1, lado + 1):
        if i == 1 or i == lado:  
            figura += "*" * lado + "\n"
        else:
            
            figura += "*" + " " * (lado - 2) + "*\n"
    return figura

main()
