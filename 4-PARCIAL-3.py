from apoyo import mostrar_mensaje
from inventario import crear_producto_inventario

def main():
    inventario = crear_datos_inventario()
    mostrar_mensaje(inventario)

def crear_datos_inventario():
    inventario = {
        "A123": {
            "codigo": "A123",
            "nombre": "Memoria USB 32 MB",
            "cantidad": 10
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

main()
