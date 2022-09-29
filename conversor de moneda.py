
# #Menú de opciones
# exchange = int(input("""Elige el tipo de cambio que deseas hacer digitando el número de la opción deseada:
#                     1. de pesos a dolares
#                     2. de dolares a pesos.\n"""))

# match exchange:
#     case 1:
#         valDolares = float(input("Ingrese el valor del dolar a hoy: "))
#         cantidad = float(input("Ingrese el dinero en pesos, que desea cambiar: "))

#         calculo = str(cantidad  / valDolares)
#         cambio = round(float(calculo), 2)
#     case 2:
#         valPesos = float(input("Ingrese el valor representativo del peso a hoy: "))
#         cantidad = float(input("Ingrese la cantidad de dolares, que desea cambiar: "))

#         calculo = str(cantidad * valPesos)
#         cambio = float(calculo)

# #respuesta
# print ("El valor equivalente de su cambio de moneda es: " + str(cambio))


def conversor (tipo_moneda, valDolares):
    cantidad = float(input("Ingrese el dinero en pesos Colombianos, que desea cambiar: "))

    calculo = str(cantidad  / valDolares)
    cambio = round(float(calculo), 2)

    print ("El valor equivalente de su cambio de moneda es: " + str(cambio)) 

menu = """ 
Bienvenido al conversor de monedas 
1 - Pesos Colombianos
2 - Pesos Argentinos
3 - Pesos Mexicanos

Elie una opción: """

opcion = int(input(menu))

if opcion == 1:
    conversor("Colombianos", float(input("Valor del dolar a hoy: ")))
elif opcion == 2:
    conversor("Argentinos", float(input("Valor del dolar a hoy: ")))
elif opcion == 3:
    conversor("Mexicanos", float(input("Valor del dolar a hoy: ")))
else:
    print ("Ingresa una opción correcta, por favor.")
