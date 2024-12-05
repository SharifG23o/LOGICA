


from apoyo import mostrar_mensaje
from inventario import crear_producto_inventario


def main():
    
    producto=crear_producto_inventario("A123", "Memorias USB 32MB",10)
    mensaje=convertir_producto_mensaje(producto)
    mostrar_mensaje(mensaje)

def convertir_producto_mensaje(producto):
   mensaje = " "
   for codigo, producto in producto.items():
        mensaje+=f"{codigo}: {producto['nombre']}\t {producto['cantidad']}\n"
        
   return mensaje
   
 

main()