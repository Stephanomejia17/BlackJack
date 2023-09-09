class Carta:
    def __init__(self, pinta: str, valor: str):
        self.pinta: str = pinta
        self.valor: str = valor
        self.tapada: bool = False


class Mano:
    def __init__(self, cartas: tuple[Carta, Carta]):
        self.cartas: list[Carta] = []

    def es_blackjack(self) -> bool:
        pass


class Baraja:
    def __init__(self):
        self.cartas: list[Carta] = []

    def revolver(self):
        pass
    def repartir_carta(self, tapada: bool) -> Carta:
        pass
    def solicitar_carta(self) -> Carta:
        pass

class Jugador:
    def __init__(self, nombre: str, fichas: int):
        self.nombre: str = nombre
        self.fichas: int = fichas
        self.mano: Mano = None

    def inicializar_mano(self, cartas: tuple[Carta, Carta]):
        pass
    def plantarse(self):
        pass

class Casa:
    def __init__(self):
        self.mano: Mano = None

    def inicializar_mano(self, cartas: tuple[Carta, Carta]):
        pass
    def plantarse(self):
        pass
    def destapar(self):
        pass

class BlackJack:
    def __init__(self):
        self.jugador: Jugador = None
        self.cupier: Casa = None
        self.baraja: Baraja = None

    def registrar_jugador(self, nombre: str):
        pass

    def iniciar_juego(self, apuesta: int):
        pass

    def preguntar_jugada(self):
        pass

    def comparar_manos(self, mano_jugador: Mano, mano_casa: Mano):
        pass

    def continuar_partida(self, fichas: int):
        pass
    def menu(self):
        pass
    def finalizar_juego(self):
        pass
