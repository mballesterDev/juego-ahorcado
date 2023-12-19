import random
pelis = ["titanic", "it", "interestelar", "rocky", "barbie"]
letras = []

def peliRandom():
    for i in range(5):
        i = random.randint(0, 4)
        peliAleatorioa = pelis[i]
        break
    
    return peliAleatorioa


peli_random = peliRandom() #y la variable peliAlwtaroria se guarda así

def palabraSplit():
    for char in peli_random:
        letras.append(char)
    

palabraSplit()

def juego():
    fallos = 0
    r1 = "z"
    for i in range(len(letras)):
        while r1 != letras[i]:
            r1 = input(f"Di la letra {i + 1} de la palabra: ")
            if r1 == letras[i]:
                print("\nCORRECTO")
            else:
                print("\nIncorrecto")
                fallos += 1
                print(f"\nTienes un total de {fallos} fallos")
                if fallos == 5:
                    print("\nCUIDADO, ESTÁS A 1 FALLO DE PERDER")
                
                if fallos ==6:
                    print("\nHAS PERDIDO")



juego()