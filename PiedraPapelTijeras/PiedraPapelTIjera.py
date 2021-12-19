import random

def jugar():
    print("Juguemos piedra papel o tijera")
    usuario = input("ESCRIBE 'pi' para sacar PIEDRA, ESCRIBE 'pa' para sacar PAPEL, ESCRIBE 'ti' para sacar TIJERAS\n").lower()
    computador = random.choice(['pi', 'pa', 'ti'])

    if usuario ==computador:
        print("¡¡¡EMPATE!!!")
    elif ganaUsuario(usuario, computador):
        print("¡¡¡GANASTE!!!")
    else:
        print("¡¡¡PERDISTE!!!")


def ganaUsuario(usuario, computador):
    #usario saca "pi" compitador saca "ti"
    #usario saca "pa" compitador saca "pi"
    #usario saca "ti" compitador saca "pa"
    if (usuario == 'pi' and computador == 'ti') or (usuario == 'pa' and computador == 'pi') or (usuario == 'ti' and computador == 'pa'):
        return True
    else:
        return False

jugar()