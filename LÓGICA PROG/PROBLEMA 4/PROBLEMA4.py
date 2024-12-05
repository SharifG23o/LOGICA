def main():
   valor_longitud=ingresar_real("el valor de la longitud es:")
   valor_ancho= ingresar_real("el valor del ancho es:")
   valor_area= calcular_valor_area(valor_longitud,valor_ancho)
   mensaje= generar_mensaje(valor_longitud, valor_ancho, valor_area)
   mostrar_mensaje(mensaje)
   
def ingresar_real(mensaje):
 real= float(input(mensaje))
 return real
	
def calcular_valor_area(valor_longitud,valor_ancho):
 valor_area= valor_longitud*valor_ancho
 return valor_area
	
def generar_mensaje(valor_longitud, valor_ancho, valor_area):
 mensaje=f"el valor de la longitud es{valor_longitud:.2f}"
 mensaje=f"el valor del ancho es{valor_ancho:8.2f}"
 mensaje=f"por lo tanto, el recipiente tiene un area de {valor_area:8.2f}"
 return mensaje
	
	
	
def mostrar_mensaje(mensaje):
 print(mensaje)
main()