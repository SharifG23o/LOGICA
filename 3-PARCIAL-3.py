
from apoyo import mostrar_mensaje, ingresar_texto,ingresar_entero_mayor_que


def main():
    inventario=ingresar_producto_inventario("Datos de un producto del inventario")
    mostrar_mensaje(inventario)

def ingresar_producto_inventario(titulo):
    mostrar_mensaje(titulo)

    codigo_producto = ingresar_texto("Ingrese el código: ")
    nombre = ingresar_texto("Ingrese el nombre del producto: ")
    cantidad= ingresar_texto("Ingrese la cantidad: ")
    producto = {
        "codigo":codigo_producto,'nombre': nombre, 'cantidad':cantidad
     } 
     # esta es la tupla
    return producto

main()
    
   