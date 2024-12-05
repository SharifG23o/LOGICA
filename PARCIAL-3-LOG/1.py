
from apoyo import mostrar_mensaje


def main():
    producto=crear_producto_inventario("A123", "Memorias USB 32MB", 10)
    mostrar_mensaje(producto)

def crear_producto_inventario(codigo,nombre,producto):
    productos={
        "A123": {"codigo": "A123",
	"nombre": "Memoria USB 32 MB",
	"cantidad": 10}
  }
    

main()