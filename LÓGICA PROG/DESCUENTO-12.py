""""
Programa para determinar el descuento según día de nacimiento y género 
Autor: Area de programacion UQ
Fecha: Febrero 2024
Licencia: GNU GPL v3
def ma"""
from apoyo import ingresar_texto, ingresar_real, ingresar_entero, mostrar_mensaje 

in():
     genero= ingresar_texto("Ingrese su genero:").lower()
     dia_nacimiento=ingresar_texto("Ingrese su día de nacimiento: ")
     valor_cuenta=ingresar_real("Ingrese el valor de su cuenta")
     calcular_porcentaje_descuento= determinar_porcentaje_descuento("genero, dia_nacimiento, valor_cuenta")
     calcular_valor_final= determinar_valor_final("valor_cuenta, determinar_porcentaje_descuento")
     mensaje_descuento= generar_mensaje_descuento("genero, dia_nacimiento, determinar_porcentaje_descuento")
     mostrar_mensaje(mensaje_descuento)

def determinar_porcentaje_descuento():
  if genero=="mujer":
      if dia_nacimiento%2==0: 
          #par 
      else: 
          
          #impar

if genero=="hombre":
    if dia_nacimiento>=3 and dia_nacimiento<=14 or dia_nacimiento>=17 and dia_nacimiento<=21
    descuento=0.10
    elif dia_nacimiento>=1 and dia_nacimiento<=2 
    descuento=0.07
elif dia_nacimiento >=15 and dia_nacimiento<=16 
    descuento=0.09
else: 
    return 0.03

 

        
      



def determinar_valor_final(cuenta,descuento):
     return cuenta-determinar_porcentaje_descuento

def generar_mensaje_descuento(genero, dia_nacimiento,descuento):
     mensaje= f"Con su género {genero}, su fecha de nacimiento {dia_nacimiento} y el valor de su cuenta {valor_cuenta}, su valor final a pagar es de {determinar_valor_final}"
     return mensaje

main()
     

     


        
    

     





