
######### INICIO FUNCIONES ###############

def conversor (tipo_moneda, valDolares):
    cantidad = int(input("Ingrese el dinero en pesos Colombianos, que desea cambiar: "))

    calculo = str(cantidad  / valDolares)
    cambio = round(float(calculo), 2)

    print ("El valor equivalente de su cambio de moneda es: " + str(cambio)) 

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
exchange = int(input("""Elige el tipo de cambio que deseas hacer digitando el número de la opción deseada:
                    1. Pesos Colombianos
                    2. Pesos Argentinos
                    3. Pesos Mexicanos.\n"""))

match exchange:
    case 1:
        conversor("Colombianos", float(input("Valor del dolar a hoy: ")))
    case 2:
        conversor("Argentinos", float(input("Valor del dolar a hoy: ")))
    case 3:
        conversor("Mexic", float(input("Valor del dolar a hoy: ")))

######### INICIO MENU con match y cases python 3.10 ###############