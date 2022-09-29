
##def imprimir_mensaje ():
##print ("Mensaje Especial")
##print("estoy aprendiendo a usar funciones.")
##
##imprimir_mensaje()    
##imprimir_mensaje()
##imprimir_mensaje()

def conversacion (mensaje):
    print ('Hola')
    print ('Como estas')
    print ('Elegiste la opción 1')
    print ('Adios')    

opcion = int(input("elige una opción (1, 2, 3): "))

if  opcion == 1:
    conversacion('Elegiste la opción 1')
elif opcion == 2:
    conversacion('Elegiste la opción 2')
elif opcion == 3:
    conversacion('Elegiste la opción 3')    
else:
    print ('Escribe una opción correcta')


