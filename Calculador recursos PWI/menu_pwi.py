
def run():
    nombres = input('Escriba su nombre: ').upper
    nickname = input('Escribe del nickname de tu pj: (digita player1, si prefieres omitirlo): ').upper
    server = int(input(
        """Elija el server en el que juega: 
            1. Tideswell (TI)
            2. Dawnliht (DA)
            3. Twilight (TW)
            """))
    raza = int(input(
        """Elija el número que corresponde a la raza de su pj: 
            1. Winged Elf
            2. Tideborn
            3. Untamed
            4. EarthGuard
            5. Humans
            6. NightShade
            """))

    if raza == 1:
        clase = int(input(
            """Elija el número que corresponde a la clase de su pj: 
            1. Archer
            2. Cleric
            3. EdgeRunner 
            """))
    elif raza == 2:
        clase = int(print(
            """Elija el número que corresponde a la clase de su pj: 
            1. Assasin
            2. Physic 
            """))
    elif raza == 3:
        clase = int(print(
            """Elija el número que corresponde a la clase de su pj: 
            1. Barbarian
            2. Venomancer
            3. Wildwalker 
            """))
    elif raza == 4:
        clase = int(print(
            """Elija el número que corresponde a la clase de su pj: 
            1. Seeker
            2. Mystic 
            """))
    elif raza == 5:
        clase = int(print(
            """Elija el número que corresponde a la clase de su pj: 
            1. Blademaster
            2. Wizard 
            3. Technician
            """))
    elif raza == 6:
        clase = int(print(
            """Elija el número que corresponde a la clase de su pj: 
            1. Duskblade
            2. Stormbringer 
            """))








if __name__ == '__main__':
    run()