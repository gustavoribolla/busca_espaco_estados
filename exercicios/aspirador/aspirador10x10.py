from aigyminsper.search.SearchAlgorithms import BuscaCustoUniforme, BuscaLargura, AEstrela
from aigyminsper.search.Graph import State
import time
# import networkx as nx
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

        if self.direcao == "e":
            s1 = AspiradorPo('girar_esquerda', self.position, 'b', self.mapa)
            successors.append(s1)
        if self.direcao == 'b':
            s2 = AspiradorPo('girar_esquerda', self.position, 'd', self.mapa)
            successors.append(s2)
        if self.direcao == 'd':
            s3 = AspiradorPo('girar_esquerda', self.position, 'c', self.mapa)
            successors.append(s3)
        if self.direcao == 'c':
            s4 = AspiradorPo('girar_esquerda', self.position, 'e', self.mapa)
            successors.append(s4)



        if self.direcao == "e":
            s1 = AspiradorPo('girar_direita', self.position, 'c', self.mapa)
            successors.append(s1)
        if self.direcao == 'c':
            s2 = AspiradorPo('girar_direita', self.position, 'd', self.mapa)
            successors.append(s2)
        if self.direcao == 'd':
            s3 = AspiradorPo('girar_direita', self.position, 'b', self.mapa)
            successors.append(s3)
        if self.direcao == 'b':
            s4 = AspiradorPo('girar_direita', self.position, 'e', self.mapa)
            successors.append(s4)

        
        if (self.position[0] != 0) and self.direcao == 'e':
            self.mapa[self.position] = 1
            self.position[0] = self.position[0]-1
            s5 = AspiradorPo('mover_frente', self.position, self.direcao, self.mapa)
            successors.append(s5)

        if (self.position[1] != 0) and self.direcao == 'c':
            self.mapa[self.position] = 1
            self.position[1] = self.position[1]-1
            s5 = AspiradorPo('mover_frente', self.position, self.direcao, self.mapa)
            successors.append(s5)

        if (self.position[0] != 9) and self.direcao == 'd':
            self.mapa[self.position] = 1
            self.position[0] = self.position[0]+1
            s5 = AspiradorPo('mover_frente', self.position, self.direcao, self.mapa)
            successors.append(s5)

        if (self.position[1] != 9) and self.direcao == 'b':
            self.mapa[self.position] = 1
            self.position[1] = self.position[1]+1
            s5 = AspiradorPo('mover_frente', self.position, self.direcao, self.mapa)
            successors.append(s5)

        #limpar
        if self.mapa[self.position[0]][self.position[1]] == 0:
            self.mapa[self.position[0]][self.position[1]] = 1
            s6 = AspiradorPo('limpar', self.position,self.direcao, self.mapa)
            successors.append(s6)
        
        return successors

    def env(self):
        return self.position

    # def h(self):
    #     return (abs(self.position[0] - self.pos_fim[0]) + abs(self.position[1] - self.pos_fim[1]))

    def description(self):
        return "Aspirador"

    def cost(self):
        return 1
    
    def is_goal(self):
        if 0 in self.mapa[0] or 0 in self.mapa[1] or 0 in self.mapa[2] or 0 in self.mapa[3] or 0 in self.mapa[4] or 0 in self.mapa[5] or 0 in self.mapa[6] or 0 in self.mapa[7] or 0 in self.mapa[8] or 0 in self.mapa[9]:
            return True
        return False
    

def main():
    mapa = []
    for _ in range(10):
        lista_interna = [random.randint(0, 1) for _ in range(10)]
        mapa.append(lista_interna)
    state = AspiradorPo('', (0, 0), 'd', mapa)
    algorithm = BuscaLargura()
    result = algorithm.search(state, trace=True)

    if result is not None:
        print("Caminho encontrado:")
        print(result.show_path())
        print(f"Custo: {result.g}")
    else:
        print("Nenhum caminho encontrado")

if __name__ == "__main__":
    main()