import random
print("Bienvenido al juego ADIVINA el numero || Desarrollado por Jesus :3")
print("Para jugarlo es muy sencillo")
print("Solo ingresas un numero entre 1 y 100")
print("Si escogiste al numero igual que el de la maquina")
print("Felicitaciones, le ganaste, en caso contrario lo podras volver a intentar")
print("Suerte!")

numero_aleatorio = random.randint(1, 100)
acerto = False
contador = 0
while acerto != True:
    numero_jugador = input('Ingresa el numero: ')
    numero_jugador = int(numero_jugador)
    if(numero_jugador >= 1 and numero_jugador <=100):
        if (numero_jugador == numero_aleatorio):
            print("En hora buena, por fin encontraste el numero")
            print("Para llegar hasta aqui, lo intentaste", contador, "veces")
            print(" ")
            print("Quieres volver a jugar?, en caso afirmativo escribe si")
            escoger = input(" ")
            if (escoger == 'si'):
                print("En hora buena, empezemos de nuevo, !SUERTE¡")
                numero_aleatorio = random.randint(1, 100)
                contador = 0
                acerto = False
            else:
                print("Tes esperamos para la proxima")
                contador = 0
                acerto = True

        elif (numero_jugador > numero_aleatorio):
            print("Tu numero es mayor al del ROBOT, intenta Bajarlo")
            contador = contador + 1
        else:
            print("Tu numero es menor al del ROBOT, intenta Subirlo")
            contador = contador + 1
    else:
        print("Recuerda que el numero debe ser entre 1 y 100")



print(numero_aleatorio)