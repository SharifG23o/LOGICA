""""
Programa para determinar el aumento en el recibo del agua
Autor: Area de programacion UQ
Fecha: Febrero 2024
Licencia: GNU GPL v3
"""











def determinar_porcentaje_aumento(consumo):

    if consumo>= 1 and consumo<=9:
        porcentaje_aumento= 0.15

    else:
        if consumo>=13 and consumo<= 15:
            porcentaje_aumento= 0.15 

        else: 
            if consumo>=20 and consumo<=28: 
                porcentaje_aumento=0.25 

            else: 
                porcentaje_aumento= 0.03 

    return porcentaje_aumento


