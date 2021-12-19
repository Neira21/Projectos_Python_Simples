import random

print("Bienvenido(a), elige el nivel de dificultad")
print("Opción 1 Fácil: 1 al 10")
print("Opción 2 Intermedio: 1 al 30")
print("Opción 3 Difícil: 1 al 100")


def jugarAdivinaNúmero(x):
    print("=========================================================")
    print("Bienvenido(a), al juego")
    print("=========================================================")
    print("Tu meta es adivinar el número generado por la computadora")
    print("en el menor número de intentos posibles")
    numero_aletario=random.randint(1,x)

    numero_usuario = 0
    intentos = 0

    while numero_usuario != numero_aletario:
        numero_usuario=int(input("\nUsuario, adivina el número "))
        if numero_usuario<numero_aletario:
            print("Intenta otra vez, este número es muy pequeño")
            intentos+=1
        elif numero_usuario>numero_aletario:
            print("Intenta otra vez, este número es muy grande")
            intentos+=1
    print(f"¡Felicidades! Adivinaste el número {numero_aletario} correctamente y solo te tomaron {intentos} intentos")

while True:
    opcion = int(input("\nElija un nivel o pulse 4 para acabar el programa "))
    if opcion == 1:
        jugarAdivinaNúmero(10)
    elif opcion == 2:
        jugarAdivinaNúmero(30)
    elif opcion == 3:
        jugarAdivinaNúmero(100)
    elif opcion == 4:
        break
    else:
        print("\nElija una opción correcta entre 1 al 3 ")

print("Juego terminado, gracias por jugar")