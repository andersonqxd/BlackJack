import random

class Baralho:
    def __init__(self):
        self.__cartas = {
            '2':2,
            '3':3,
            '4':4,
            '5':5,
            '6':6,
            '7':7,
            '8':8,
            '9':9,
            '10':10,
            'J':10,
            'Q':10,
            'K':10,
            'A':[1, 11]
        }
        self.deeler  = []
        self.jogador = []
        
    def darCartas(self):
        i = 0
        while i < len(self.__cartas) // 2:
            naipe = random.choices(list(self.__cartas.keys()))
            self.deeler.append(naipe)
            naipe = random.choices(list(self.__cartas.keys()))
            self.jogador.append(naipe)
            i = i + 1
    
    def mostraCartas(self):
        print(' '.join(map(str, self.jogador)))
        print(' '.join(map(str, self.deeler)))
        
class BlackJack():
    def main():
        bj = Baralho()
        bj.darCartas()
        bj.mostraCartas()