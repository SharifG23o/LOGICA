from apoyo import mostrar_mensaje
from inventario import crear_datos_inventario

def main():
    inventario = crear_datos_inventario()
    productos_a_comprar = filtrar_productos_a_comprar(inventario)
    mostrar_mensaje(productos_a_comprar)

def filtrar_productos_a_comprar(inventario):
    productos_a_comprar = []
    for codigo, producto in inventario.items():
        if producto['cantidad'] < 3:
            productos_a_comprar.append((codigo, producto['cantidad']))
        
    return productos_a_comprar

main()

