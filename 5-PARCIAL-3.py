from apoyo import mostrar_mensaje
from inventario import crear_datos_inventario

def main():
    inventario=crear_datos_inventario()
    mensaje=convertir_inventario_mensaje(inventario)
    mostrar_mensaje(mensaje)

def convertir_inventario_mensaje(inventario):
    mensaje = " "
    for codigo, producto in inventario.items():
        mensaje+=f"{codigo}: {producto['nombre']}\t {producto['cantidad']}\n"
        
    return mensaje

main()