from aigyminsper.search.SearchAlgorithms import *
from aigyminsper.search.Graph import State
import json

class AspiradorPo(State):
    # Aspirador 10x10
    # Matriz 10x10, onde cada posição é um quadrado
    # Cada quadrado pode estar limpo ou sujo
    # O robô pode estar em qualquer quadrado
    # O robô pode limpar o quadrado onde está
    # O robo pode virar para esquerda ou direita e andar para frente

    def __init__(self, op, quartos, posicao_robo, direcao_robo):
        self.operator = op
        # lista de listas, onde cada lista é uma linha da matriz
        # cada elemento da lista é um quadrado
        # True = limpo
        # False = sujo
        self.quartos = quartos
        # posicao do robo
        # tupla (x, y)
        self.posicao_robo = posicao_robo
        # direcao do robo
        # 'esq', 'dir', 'cima', 'baixo'
        self.direcao_robo = direcao_robo
                
    
    def successors(self):
        successors = []
        # limpar
        if self.quartos[self.posicao_robo[0]][self.posicao_robo[1]] == False:
            s1 = AspiradorPo('limpar', self.quartos, self.posicao_robo, self.direcao_robo)
            s1.quartos[s1.posicao_robo[0]][s1.posicao_robo[1]] = True
            successors.append(s1)
        # mover para frente
        s2 = AspiradorPo('mover_frente', self.quartos, self.posicao_robo, self.direcao_robo)
        if s2.direcao_robo == 'dir' and s2.posicao_robo[1] < 9:
            s2.posicao_robo = (s2.posicao_robo[0], s2.posicao_robo[1]+1)
        elif s2.direcao_robo == 'esq' and s2.posicao_robo[1] > 0:
            s2.posicao_robo = (s2.posicao_robo[0], s2.posicao_robo[1]-1)
        elif s2.direcao_robo == 'cima' and s2.posicao_robo[0] > 0:
            s2.posicao_robo = (s2.posicao_robo[0]-1, s2.posicao_robo[1])
        elif s2.direcao_robo == 'baixo' and s2.posicao_robo[0] < 9:
            s2.posicao_robo = (s2.posicao_robo[0]+1, s2.posicao_robo[1])
        successors.append(s2)
        # virar para esquerda
        s3 = AspiradorPo('virar_esq', self.quartos, self.posicao_robo, self.direcao_robo)
        if s3.direcao_robo == 'dir':
            s3.direcao_robo = 'cima'
        elif s3.direcao_robo == 'esq':
            s3.direcao_robo = 'baixo'
        elif s3.direcao_robo == 'cima':
            s3.direcao_robo = 'esq'
        elif s3.direcao_robo == 'baixo':
            s3.direcao_robo = 'dir'
        successors.append(s3)
        # virar para direita
        s4 = AspiradorPo('virar_dir', self.quartos, self.posicao_robo,  self.direcao_robo)
        if s4.direcao_robo == 'dir':
            s4.direcao_robo = 'baixo'
        elif s4.direcao_robo == 'esq':
            s4.direcao_robo = 'cima'
        elif s4.direcao_robo == 'cima':
            s4.direcao_robo = 'dir'
        elif s4.direcao_robo == 'baixo':
            s4.direcao_robo = 'esq'
        successors.append(s4)

        return successors
    
    def is_goal(self):
        if False in self.quartos[0] or False in self.quartos[1] or False in self.quartos[2] or False in self.quartos[3] or False in self.quartos[4] or False in self.quartos[5] or False in self.quartos[6] or False in self.quartos[7] or False in self.quartos[8] or False in self.quartos[9]:
            return False
        return True
    
    def description(self):
        return """
                O aspirador de pó está em um ambiente 10x10, 
                onde cada quadrado pode estar limpo ou sujo. 
                O robô pode limpar o quadrado onde está, virar 
                para esquerda ou direita e andar para frente.
               """
    
    def cost(self):
        return 1
    
    def env(self):
        return json.dumps(self._dict_)

    def h(self):
        num_quartos_sujos = sum([sum([1 for sujo in linha if sujo == False]) for linha in self.quartos])
        if self.operator == 'limpar':
            return num_quartos_sujos - 1  # Penalize a ação de limpar
        return num_quartos_sujos

def main():
    # Lista de listas, onde cada lista é uma linha da matriz
    # cada elemento da lista é um quadrado
    # True = limpo
    # False = sujo
    quartos = [[True, False, True, True, True, False, True, False, True, False],
               [False, True, False, True, False, True, True, True, True, True],
               [True, True, True, False, True, False, True, False, True, False],
               [False, True, False, True, False, True, False, True, False, True],
               [True, False, True, False, True, False, True, False, True, False],
               [False, True, False, True, True, True, True, True, True, True],
               [True, True, True, False, True, False, False, False, False, False],
               [False, False, False, False, False, False, False, True, False, True],
               [True, False, True, False, True, False, True, False, True, False],
               [False, True, False, True, False, True, False, True, False, True]]
    state = AspiradorPo('', quartos, (0, 0), 'dir')
    print(state.description())
    algorithm = AEstrela()
    result = algorithm.search(state, trace=False, pruning='general')
    if result != None:
        print('Achou!')
        print(result.show_path())
        print(state.quartos)
    else:
        print('Nao achou solucao')

if __name__ == '__main__':
    main()