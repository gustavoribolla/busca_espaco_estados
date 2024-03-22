from aigyminsper.search.SearchAlgorithms import BuscaCustoUniforme, BuscaLargura
from aigyminsper.search.Graph import State
import time
# import networkx as nx
from config import *

MUD = '■'
END = '⚑'


class Bike(State):
    def __init__(self, operator, position, map, pos_fim, cost_):
        self.position = position
        self.map = map
        self.pos_fim = pos_fim
        self.operator = operator
        self.cost_ = cost_ 

        
    def successors(self):
        successors = []
        
        if self.position[0]> 0:
            new_pos = (self.position[0] -1, self.position[1])
            if self.map[new_pos[0]][new_pos[1]] == MUD:
                successors.append(Bike( 'up',new_pos, self.map, self.pos_fim, 4))
            else:
                successors.append(Bike( 'up',new_pos, self.map, self.pos_fim, 1))
                

        if self.position[0] < len(self.map)-1:
            new_pos = (self.position[0] + 1, self.position[1])
            if self.map[new_pos[0]][new_pos[1]] == MUD:
                successors.append(Bike('down' ,new_pos, self.map, self.pos_fim, 4))
            else:
                successors.append(Bike( 'down',new_pos, self.map, self.pos_fim, 1))
        
        if self.position[1] < len(self.map[0])-1:
            new_pos = (self.position[0], self.position[1]+ 1)
            if self.map[new_pos[0]][new_pos[1]] == MUD:
                successors.append(Bike('right' ,new_pos, self.map, self.pos_fim, 4))
            else:
                successors.append(Bike( 'right',new_pos, self.map, self.pos_fim, 1))

        if self.position[1] > 0:
            new_pos = (self.position[0], self.position[1]- 1)
            if self.map[new_pos[0]][new_pos[1]] == MUD:
                successors.append(Bike('left' ,new_pos, self.map, self.pos_fim, 4))
            else:
                successors.append(Bike( 'left',new_pos, self.map, self.pos_fim, 1))
                
        return successors

    def env(self):
        return self.position, self.cost_

    # def h(self):
    #     return (abs(self.position[0] - self.pos_fim[0]) + abs(self.position[1] - self.pos_fim[1]))

    def description(self):
        return "Bicicleta"

    def cost(self):
        return self.cost_
    
    def is_goal(self):
        return self.position == self.pos_fim
    

def main():
    # mapa = cria_mapa(5, 7, [[0,2],[0,3],[1,2],[1,3],[2,3],[0,4]],[0, 5])
    # mapa = cria_mapa(5, 7, [[0,2],[1,2],[1,3],[2,3]], [0, 5])
    mapa = cria_mapa(8, 4, [[0,3],[1,3],[2,3],[3,1],[4,1],[5,1], [6,1],[7,1]],[7, 0])
    

    map = mapa
    # Altere a posição da bike e do objetivo antes de rodar
    print(imprime_mapa(map))
    state = Bike('', (2, 2), map, (7,0), 0)
    algorithm = BuscaCustoUniforme()
    result = algorithm.search(state, trace=True)

    if result is not None:
        print("Caminho encontrado:")
        print(result.show_path())
        print(f"Custo: {result.g}")
    else:
        print("Nenhum caminho encontrado")

if __name__ == "__main__":
    main()