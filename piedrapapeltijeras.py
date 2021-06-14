from random import randint

def empezarJuego(marcador_jugador, marcador_ordenador):
    # lista piedra papel y tijeras
    opciones = ["piedra", "papel", "tijeras"]

    ordenador = opciones[randint(0,2)]

    jugador = input("Piedra, papel o tijeras: ")
    jugador = jugador.lower()

    #sume el marcador en ambos para luego devolver el ganador
    marcador_jugador = marcador_jugador + 1
    marcador_ordenador = marcador_ordenador + 1

    if jugador == ordenador:
        print("Empate")

    elif jugador == "piedra" and ordenador == "tijeras":
        print("Piedra rompe a tijeras, has ganado un punto")
        return marcador_jugador

    elif jugador == "piedra" and ordenador == "papel":
        print("Papel envuelve piedra, ordenador ha ganado un punto")
        return marcador_ordenador

    elif jugador == "papel" and ordenador == "piedra":
        print("Papel envuelve piedra, has ganado un punto")
        return marcador_jugador

    elif jugador == "papel" and ordenador == "tijeras":
        print("Tijeras corta papel, ordenador ha ganado un punto")
        return marcador_ordenador

    elif jugador == "tijeras" and ordenador == "papel":
        print("Tijeras corta papel, has ganado un punto")
        return marcador_jugador
        
    elif jugador == "tijeras" and ordenador == "piedra":
        print("Piedra rompe a tijeras, ordenador ha ganado un punto")
        return marcador_ordenador
    
    else:
        print("Jugada no válidad, revisa tu ortografía")


marcador_jugador = 0
marcador_ordenador = 0

while True:
    empezarJuego(marcador_jugador,marcador_ordenador)
    print("El marcador actual es: Jugador %d | Ordenador %d" %(marcador_jugador,marcador_ordenador))

    seguir_jugando = input("¿Quieres seguír jugando? escribe S o N")

    if seguir_jugando == n or seguir_jugando == N:
        break