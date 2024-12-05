def main():
   precio_original=ingresar_real("ingresar precio original:")
   valor_descuento= ingresar_real("ingresar valor descuento:")
   valor_pagar= calcular_valor_pagar(precio_original,valor_descuento)
   mensaje= generar_mensaje(precio_original,valor_descuento, valor_pagar)
   mostrar_mensaje(mensaje)
   
def ingresar_real(mensaje):
 real= float(input(mensaje))
 return real
	
def calcular_valor_pagar(precio_original,valor_descuento):
 valor_pagar= precio_original-valor_descuento
 return valor_pagar
	
def generar_mensaje(precio_original, valor_descuento, valor_pagar):
 mensaje=f"el valor ${valor_pagar:.2f}"
 mensaje=f"el valor ${valor_descuento:8.2f}"
 mensaje=f"el valor total a pagar es ${valor_pagar:8.2f}"
 return mensaje
	
	
	
def mostrar_mensaje(mensaje):
 print(mensaje)
main()