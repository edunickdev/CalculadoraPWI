def run():
    base = int(input('Indíque el número de la tabla que desea conocer: '))
    limite = int(input('Indíque el límite de la tabla (...hasta el 10, 100, 1000... etc.): '))
    contador = 1

    while contador <= limite:
        resultado = base * contador
        print(str(base) + ' por ' + str(contador) + ' es igual a: ' + str(resultado))
        contador += 1

if __name__ == '__main__':
    run()