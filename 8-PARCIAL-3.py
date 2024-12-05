
from apoyo import mostrar_mensaje
from inventario import crear_datos_inventario, filtrar_productos_a_comprar


def main():
    inventario=crear_datos_inventario()
    productos_a_comprar=filtrar_productos_a_comprar(inventario)
    mensaje=convertir_productos_comprar_mensaje(productos_a_comprar)
    mostrar_mensaje(mensaje)


def convertir_productos_comprar_mensaje(productos_a_comprar):
    mensaje=""
    for codigo,producto in productos_a_comprar:
         if producto < 3:
            mensaje+=f"Del producto {codigo} solamente hay {producto}\n"
        
        
                            
    return mensaje

main()