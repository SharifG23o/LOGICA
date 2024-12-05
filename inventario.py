
def crear_producto_inventario(codigo,nombre,cantidad):
    productos={
        "A123": {"codigo": "A123",
	"nombre": "Memoria USB 32 MB",
	"cantidad": 10}
  }
    return productos
    

def crear_datos_inventario():
    inventario = {
        "A123": {
            "codigo": "A123",
            "nombre": "Memoria USB 32 MB",
            "cantidad": 5
        },
        "CAB12": {
            "codigo": "CAB12",
            "nombre": "Cable de HDMI a VGA",
            "cantidad": 8
        },
        "SSD30": {
            "codigo": "SSD30",
            "nombre": "Unidad SSD de 300 GB",
            "cantidad": 0
        },
        "LAP01": {
            "codigo": "LAP01",
            "nombre": "Laptop i9 con 64 GB",
            "cantidad": 1
        }
    }
    return inventario


def filtrar_productos_a_comprar(inventario):
    productos_a_comprar = []
    for codigo, producto in inventario.items():
        if producto['cantidad'] < 3:
            productos_a_comprar.append((codigo, producto['cantidad']))
    return productos_a_comprar
