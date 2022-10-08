
######### INICIO FUNCIONES ###############

def conversoraDolar (tipo_moneda, valDolares):
    cantidad = float(input("Ingrese el dinero en su moneda, que desea cambiar: "))

    calculo = str(cantidad  / valDolares)
    cambio = round(float(calculo), 2)

    print ("El valor equivalente de su cambio de moneda es: " + str(cambio))

def conversordeDolar(tipo_moneda, cantDolares):
    cantidad = float(input("Ingrese la cantidad de Dolares que posee y desea cambiar: "))

    calculo = str(cantidad * cantDolares)
    cambio = round(float(calculo), 2)

######### FIN FUNCIONES ###############

######### INICIO MENU con If y else y elif ###############
# menu = """ 
# Bienvenido al conversor de monedas 
# 1 - Pesos Colombianos
# 2 - Pesos Argentinos
# 3 - Pesos Mexicanos

# Elie una opción: """

# opcion = int(input(menu))

# if opcion == 1:
#     conversor("Colombianos", float(input("Valor del dolar a hoy: ")))
# elif opcion == 2:
#     conversor("Argentinos", float(input("Valor del dolar a hoy: ")))
# elif opcion == 3:
#     conversor("Mexicanos", float(input("Valor del dolar a hoy: ")))
# else:
#     print ("Ingresa una opción correcta, por favor.")

######### FIN MENU ###############

######### INICIO MENU con match y cases python 3.10 ###############

#Menú de opciones


match tipoConversion:
    case 1:
        conversordeDolar("Colombianos", float(input("Indique a cuanto equivale 1 dolar en la moneda que desea convertir: ")))
    case 2:
        conversordeDolar("Argentinos", float(input("Indique a cuanto equivale 1 dolar en la moneda que desea convertir: ")))

tipoConversion = int(input("""¿Que tipo de cambio desea realizar?, digíte la opción de su preferencia:
                    1. de su moneda local a Dolar.
                    2. de dolar a su moneda local.
De momento se dispone de cambio de las siguientes monedas (Peso Colombiano, Peso Argentino, Peso Mexicano y Soles Peruanos.)"""))




exchange = int(input("""Elige el tipo de cambio que deseas hacer digitando el número de la opción deseada:
                    1. Pesos Colombianos
                    2. Pesos Argentinos
                    3. Pesos Mexicanos.
                    4. Soles Peruanos. \n"""))

match exchange:
    case 1:
        conversoraDolar("Colombianos", float(input("Valor del dolar a hoy: ")))
    case 2:
        conversoraDolar("Argentinos", float(input("Valor del dolar a hoy: ")))
    case 3:
        conversoraDolar("Mexicanos", float(input("Valor del dolar a hoy: ")))
    case 4:
        conversoraDolar("Soles Peruanos", float(input("Valor del dolar a hoy: ")))

######### INICIO MENU con match y cases python 3.10 ###############