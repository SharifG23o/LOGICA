from apoyo import mostrar_mensaje, ingresar_texto
from inventario import crear_datos_inventario

def main():
    inventario=crear_datos_inventario()
    codigo_interes=ingresar_texto("Ingrese el código de interés: ")
    hay_producto=verificar_existencia(inventario,codigo_interes)
    mensaje=generar_mensaje_inventario(hay_producto, codigo_interes)
    mostrar_mensaje(mensaje)

def verificar_existencia(inventario,codigo_interes):
	
	if codigo_interes in inventario.keys():
		existencia_interes=inventario[codigo_interes]
	else:
		existencia_interes=None
	return existencia_interes

def generar_mensaje_inventario(hay_producto, codigo_interes):
	if hay_producto==None:
		mensaje=f"El producto no está en el inventario o sin existencias"
	else:
		mensaje=f"El código {codigo_interes}, corresponde al producto {hay_producto['nombre']} con cantidad {hay_producto['cantidad']}"
	return mensaje

main()