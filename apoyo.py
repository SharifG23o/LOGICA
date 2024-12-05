""""
Modulo de funciones
Autor: Area de programacion UQ
Fecha: Febrero 2024
Licencia: GNU GPL v3
"""
USAR_TK= True

if USAR_TK:
    from tkinter import Tk, messagebox,simpledialog
    tk=Tk()
    tk.geometry("0x0")

def ingresar_entero_mayor_que(mensaje, valor_minimo):
    repetir = True
    while repetir:
        valor = ingresar_entero(mensaje)
        if valor > valor_minimo:
            repetir = False
        else:
             mostrar_error(f"El valor no es mayor que {valor_minimo}")

    return valor



#FUNCIÓN DE INGRESAR TEXTO

def ingresar_texto(mensaje):
    if USAR_TK:
        texto=simpledialog.askstring("Entrada", mensaje)
    else:
        texto = input(mensaje)
    return texto


#FUNCIÓN DE INGRESAR ENTERO

def ingresar_entero(mensaje):
    repetir = True
    while repetir:
        try:
            entero = int(ingresar_texto(mensaje))
            repetir = False
        except:
             mostrar_error("Error, no ingresó un entero")
    return entero

#FUNCIÓN DE INGRESAR REAL

def ingresar_real(mensaje):
    repetir = True
    while repetir:
        try:
            real = float(ingresar_texto(mensaje))
            repetir = False
        except:
             mostrar_error("Error, no ingresó un real")
    return real

#FUNCIÓN DE MOSTRAR MENSAJE

def mostrar_mensaje(mensaje):
    if USAR_TK:
        messagebox.showinfo("Información", mensaje)
    else:
         print(mensaje)


#FUNCIÓN DE MOSTRAR ERROR

def mostrar_error(mensaje):
    if USAR_TK:
        messagebox.showerror("Error", mensaje)
    else:
         print(mensaje)

#FUNCIÓN DE CALCULAR PROMEDIO

def calcular_promedio(valor1, valor2, valor3, valor4, valor5):
    promedio = (valor1 + valor2 + valor3 + valor4 + valor5) / 5
    return promedio

#FUNCIÓNDE INGRESAR REAL EN UN RANGO

def ingresar_real_rango(mensaje, valor_minimo, valor_maximo):
    repetir = True
    while repetir:
        valor = ingresar_real(mensaje)
        if valor < valor_minimo or valor > valor_maximo:
             mostrar_error(f"El valor no está entre {valor_minimo} y {valor_maximo}")
        else:
            repetir = False
    return valor

#FUNCIÓN DE INGRESAR ENTERO EN UN RANGO

def ingresar_entero_rango(mensaje, valor_minimo, valor_maximo):
    repetir = True
    while repetir:
        valor = ingresar_entero(mensaje)
        if valor < valor_minimo or valor > valor_maximo:
             mostrar_error(f"El valor no está entre {valor_minimo} y {valor_maximo}")
        else:
            repetir = False
    return valor

#FUNCIÓN PARA GENERAR UN LISTADO

def generar_listado2(valor_inicial, valor_final):
    listado = ""
    i = valor_inicial
    while i <= valor_final:
        listado += f"{i:3d}.______________________________________\n."
        i = i+1
    return listado


def generar_listado(valor_inicial, valor_final):
    listado = ""
    for i in range(valor_inicial, valor_final):
        listado += f"{i:3d}.______________________________________\n."
    return listado

#FUNCIÓN PARA MOSTRAR TABLAS DE MULTIPLICAR
def generar_mensaje_tabla_multiplicar(numero_tabla, minimo_valor, maximo_valor):
    mensaje_tabla = f"\n  TABLA DE MULTIPLICAR DEL {numero_tabla}\n\n "
    i = minimo_valor
    while i <= maximo_valor:
        producto = numero_tabla*i
        mensaje_tabla += f"{numero_tabla:2d}x{i:2d}={producto:3d}\n"
        i += 1
    return mensaje_tabla


def generar_mensaje_tabla_multiplicar2(numero_tabla, minimo_valor, maximo_valor):
    mensaje_tabla = f"\n  TABLA DE MULTIPLICAR DEL {numero_tabla}\n\n "
    
    for i in range (minimo_valor, maximo_valor+1):
        producto = numero_tabla*i
        mensaje_tabla += f"{numero_tabla:2d}x{i:2d}={producto:3d}\n"
        i += 1
    return mensaje_tabla

# FUNCIÓN PARA VERIFICAR SI ES UNA VOCAL

def verificar_es_vocal(letra):
    es_vocal=letra.lower() in "aeiou"
    return es_vocal

#FUNCIÓN PARA CONVERTIR DE BINARIO A DECIMAL

def convertir_binario_decimal(numero_binario):
    valor=0
    potencia=0
    i=len(numero_binario)-1
    while i>=0:
        valor=valor+int(numero_binario[i])*2**potencia
        potencia=potencia+1
        i=i-1
    return valor

#FUNCIÓN PARA CONVERITIR DE DECIMAL A BINARIO
def convertir_decimal_binario(numero_decimal):
    numero_binario=" "
    for i in range (0,len(numero_decimal)):
        numero_binario=str(numero_decimal%2)+numero_binario
        numero_decimal=numero_decimal//2
    return numero_binario

def obtener_codigos_ascii(mensaje):
    codigos_ascii=" "
    for letra in mensaje:
        codigos_ascii+=f"{ord(letra)}"
    return codigos_ascii




def ingresar_empleado(mensaje):

    mostrar_mensaje(mensaje)
    codigo_empleado = ingresar_texto("Ingrese el código: ")
    nombre = ingresar_texto("Ingrese el nombre del empleado")
    apellido = ingresar_texto("Ingrese los apellidos o apellido: ")
    edad = ingresar_entero("Ingrese la edad: ")
    sueldo = ingresar_entero("Ingrese el sueldo: ")
    empleado = (codigo_empleado, nombre, apellido,
                edad, sueldo)  
    return empleado



def convertir_empleado_mensaje(empleado):
    

    codigo_empleado, nombre, apellido, edad, sueldo = empleado 

    mensaje = f"{codigo_empleado}: {nombre}, {apellido}, con edad {edad} años gana {sueldo}\n"

    return mensaje

def ingresar_n_textos(mensaje,cantidad):
    textos=[" "]*cantidad
    for i in range(0,len(textos)):
        textos[i]=ingresar_texto(f"{mensaje} ({i+1}) de {cantidad}: ")
    return textos

def ingresar_n_real_rango(mensaje, cantidad, valor_minimo, valor_maximo):
    valores = [0.0] * cantidad
    for i in range(len(valores)):
        valores[i] = ingresar_real_rango(f"{mensaje} ({i + 1} de {cantidad}): ", valor_minimo, valor_maximo)
    return valores

def ingresar_n_entero_rango(mensaje, cantidad, valor_minimo, valor_maximo):
    valores = [0] * cantidad
    for i in range(len(valores)):
        valores[i] = ingresar_entero_rango(f"{mensaje} ({i + 1} de {cantidad}): ", valor_minimo, valor_maximo)
    return valores

def ingresar_n_entero_mayor_que(mensaje, cantidad, valor_minimo):
    valores = [0] * cantidad
    for i in range(len(valores)):
        valores[i] = ingresar_entero_mayor_que(f"{mensaje} ({i + 1} de {cantidad}): ", valor_minimo)
    return valores

def obtener_elementos(lista):
    mensaje = ""
    for elemento in lista:
        mensaje += f"{elemento}\n"
    return mensaje
