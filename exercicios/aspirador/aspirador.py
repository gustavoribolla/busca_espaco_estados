from aigyminsper.search.SearchAlgorithms import BuscaCustoUniforme, BuscaLargura, AEstrela, BuscaProfundidadeIterativa
from aigyminsper.search.Graph import State
import time
import numpy as np
import random


class AspiradorPo(State):
    def __init__(self, operator, position, direcao, mapa):
        self.position = position
        self.mapa = mapa
        self.operator = operator
        self.direcao = direcao

    def successors(self):
        successors = []

        successors.append(AspiradorPo('girar_esquerda', self.position, turn_left(self.direcao), self.mapa))
        successors.append(AspiradorPo('girar_direita', self.position, turn_right(self.direcao), self.mapa))

        # Gerar sucessores para mover para frente
        new_position = move_forward(self.position, self.direcao)
        if new_position != self.position:
            successors.append(AspiradorPo('mover_frente', new_position, self.direcao, self.mapa))

        # Gerar sucessor para limpar
        if self.mapa[self.position[0]][self.position[1]] == 0:
            mapa_copy = [row[:] for row in self.mapa]  # Copiar o mapa para não modificar o estado atual
            mapa_copy[self.position[0]][self.position[1]] = 1
            successors.append(AspiradorPo('limpar', self.position, self.direcao, mapa_copy))

        return successors

    def env(self):
        return self.position
    
    def h(self):
        dirty_squares = [(i, j) for i in range(10) for j in range(10) if self.mapa[i][j] == 0]
        if dirty_squares:
            return min(abs(self.position[0] - x) + abs(self.position[1] - y) for x, y in dirty_squares)
        else:
            return 0

    def description(self):
        return "Aspirador"

    def cost(self):
        return 1

    def is_goal(self):
        return all(all(square == 1 for square in row) for row in self.mapa)

def turn_left(direcao):
    directions = {'e': 'b', 'b': 'd', 'd': 'c', 'c': 'e'}
    return directions[direcao]

def turn_right(direcao):
    directions = {'e': 'c', 'c': 'd', 'd': 'b', 'b': 'e'}
    return directions[direcao]

def move_forward(position, direcao):
    x, y = position
    if direcao == 'e':
        new_x = max(x - 1, 0)
        return (new_x, y)
    elif direcao == 'c':
        new_y = max(y - 1, 0)
        return (x, new_y)
    elif direcao == 'd':
        new_x = min(x + 1, 9)
        return (new_x, y)
    elif direcao == 'b':
        new_y = min(y + 1, 9)
        return (x, new_y)


def main():
    mapa = [[random.randint(0, 1) for _ in range(10)] for _ in range(10)]
    state = AspiradorPo('', (0, 0), 'd', mapa)
    algorithm = AEstrela()
    result = algorithm.search(state, trace=True, pruning="general")

    if result is not None:
        print("Caminho encontrado:")
        print(result.show_path())
        print(f"Custo: {result.g}")
    else:
        print("Nenhum caminho encontrado")

if __name__ == "__main__":
    main()