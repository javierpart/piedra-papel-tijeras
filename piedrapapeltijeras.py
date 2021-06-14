from random import randint

def empezarJuego():
    # lista piedra papel y tijeras
    opciones = {0 : "piedra",1 : "papel", 2 :"tijeras"}

    ordenador = opciones[randint(0,2)]

    # pedimos un numero entre el 0 y el 2
    while True:
        try:
            num = int(input("0-Piedra, 1-papel o 2-tijeras: "))
            if num >= 0 and num <= 2:
                jugador = opciones[num]
                break
            else:
                print("Introduce un número entre el 0 y el 2!!")
        except ValueError:
            print("Dato no valido!!")


    #sume el marcador en ambos para luego devolver el ganador
    global marcador_jugador
    global marcador_ordenador



    if jugador == ordenador:
        print("Empate")

    elif (jugador=="piedra" and ordenador=="tijeras") or (jugador=="papel" and ordenador=="piedra") or (jugador=="tijeras" and ordenador=="papel"):
        print(jugador + " gana a " + ordenador)
        marcador_jugador = marcador_jugador +1
        return marcador_jugador
        
    # no seria necesaria la comprobacion, se podria meter en un else
    elif (jugador=="tijeras" and ordenador=="piedra") or (jugador=="piedra" and ordenador=="papel") or (jugador=="papel" and ordenador=="tijeras"):
        print(ordenador + " gana a " + jugador)
        marcador_ordenador = marcador_ordenador + 1
        return marcador_ordenador



marcador_jugador = 0
marcador_ordenador = 0

while True:
    empezarJuego()
    print("El marcador actual es: Jugador %d | Ordenador %d" %(marcador_jugador,marcador_ordenador))

    seguir_jugando = input("¿Quieres seguír jugando? escribe S o N: ")

    if seguir_jugando == "n" or seguir_jugando == "N":
        break
