texto="Hola Colombia"
salida=""

i=0

while i<len(texto):
    c= texto[i]
    salida+=f"({c})"
    i=i+1

print(salida)