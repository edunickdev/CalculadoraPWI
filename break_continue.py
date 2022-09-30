def run():
    texto = input ('Escribe un texto: ')
    for letra in texto:
        if letra == 'o':
            break   
        print(letra)        

    # for i in range(10000):
    #     if i == 5678:
    #         break

    # for contador in range (1000):
    #     if contador % 2 != 0:
    #         continue
    #     print(contador)



if __name__ == '__main__':
    run()