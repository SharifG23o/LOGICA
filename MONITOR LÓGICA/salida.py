
def generar(n):
    salida="*"*n 

    for i in range (1,n-1):
        salida+= "*"+" "* (n-2)+"*"
        salida+="*"*n

    return salida