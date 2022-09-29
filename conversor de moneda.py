
#Menú de opciones
from msilib import datasizemask


exchange = int(input("""Elige el tipo de cambio que deseas hacer digitando el número de la opción deseada:
                    1. de pesos a dolares
                    2. de dolares a pesos.\n"""))

match exchange:
    case 1:
        valDolares = float(input("Ingrese el valor del dolar a hoy: "))
        cantidad = float(input("Ingrese el dinero en pesos, que desea cambiar: "))

        calculo = str(cantidad  / valDolares)
        cambio = round(float(calculo), 2)
    case 2:
        valPesos = float(input("Ingrese el valor representativo del peso a hoy: "))
        cantidad = float(input("Ingrese la cantidad de dolares, que desea cambiar: "))

        calculo = str(cantidad * valPesos)
        cambio = float(calculo)

<<<<<<< HEAD
#respuesta
print ("El valor equivalente de su cambio de moneda es: " + str(cambio))



=======
#resultado
print ("El valor equivalente de su cambio de moneda es: " + str(cambio))

>>>>>>> d80e1232c3d6681cd51e65e806e0e44b1959de41
