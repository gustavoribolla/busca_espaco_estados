from aigyminsper.search.SearchAlgorithms import BuscaLargura, BuscaProfundidade, BuscaCustoUniforme, BuscaProfundidadeIterativa, BuscaGananciosa, AEstrela
from aigyminsper.search.Graph import State
import json
import time
import copy
import math
import csv


class Deslizante(State):

    @staticmethod
    def csv_para_lista_de_listas(arquivo_csv):
        lista_de_listas = []
        with open(arquivo_csv, newline='') as csvfile:
            leitor = csv.reader(csvfile, delimiter=',')
            for linha in leitor:
                lista_de_inteiros = [int(valor) for valor in linha]
                lista_de_listas.append(lista_de_inteiros)
        return lista_de_listas

    def __init__(self, op, mapa,pos_vazio, cost):
        # You must use this name for the operator!
        self.operator = op
        self.mapa = mapa
        self.cost_ = cost
        self.pos_vazio = pos_vazio
 
 

    def successors(self):
        

        print(self.mapa)
        successors = []
        x, y = self.pos_vazio
        mapa_novo = copy.deepcopy(self.mapa)
        if x + 1 < len(mapa_novo):
            mapa_novo = copy.deepcopy(self.mapa)
            valor = mapa_novo[x+1][y] 
            mapa_novo[x][y] = valor
            mapa_novo[x+1][y] = 9
            successors.append(Deslizante("troca com debaixo", mapa_novo, (x+1,y), 1))
        if x-1>=0:
            mapa_novo = copy.deepcopy(self.mapa)
            valor = mapa_novo[x-1][y] 
            mapa_novo[x][y] = valor
            mapa_novo[x-1][y] = 9
            successors.append(Deslizante("troca com de cima", mapa_novo, (x-1,y), 1))
        if y - 1 >= 0:
            mapa_novo = copy.deepcopy(self.mapa)
            valor = mapa_novo[x][y-1] 
            mapa_novo[x][y] = valor
            mapa_novo[x][y-1] = 9
            successors.append(Deslizante("troca com da esquerda", mapa_novo, (x,y-1), 1))
        if y + 1 < len(mapa_novo[0]):
            mapa_novo = copy.deepcopy(self.mapa)
            valor = mapa_novo[x][y+1] 
            mapa_novo[x][y] = valor
            mapa_novo[x][y+1] = 9
            successors.append(Deslizante("troca com da direita", mapa_novo, (x,y+1), 0))
        return successors
    
    def is_goal(self):
        
        ordenado = True
        contador = 1
        for i in range(len(self.mapa)):
            for j in range(len(self.mapa[i])):
                if self.mapa[i][j]  != contador:
                    ordenado = False
                contador += 1
        return ordenado == True
    
    def description(self):
        return 'Problema do Deslizante'
    
    def cost(self):
        
        
        return self.cost_
    
    def env(self):
        #
        # IMPORTANTE: este método não deve apenas retornar uma descrição do environment, mas 
        # deve também retornar um valor que descreva aquele nodo em específico. Pois 
        # esta representação é utilizada para verificar se um nodo deve ou ser adicionado 
        # na lista de abertos.
        #
        # Exemplos de especificações adequadas: 
        # - para o problema do soma 1 e 2: return str(self.number)+"#"+str(self.cost)
        # - para o problema das cidades: return self.city+"#"+str(self.cost())
        #
        # Exemplos de especificações NÃO adequadas: 
        # - para o problema do soma 1 e 2: return str(self.number)
        # - para o problema das cidades: return self.city
        #
        return json.dumps(self._dict_)
    
    def h(self):
        dict = {
            1:(0,0),
            2:(0,1),
            3:(0,2),
            4:(1,0),
            5:(1,1),
            6:(1,2),
            7:(2,0),
            8:(2,1),
            9:(2,2)
        }
        heuristica = 0
        for i in range(len(self.mapa)):
            for j in range(len(self.mapa[i])):
                numero = self.mapa[i][j]
                heuristica += math.dist((i,j), (dict[numero][0], dict[numero][1]))
                
        return heuristica

def main():

    

# Exemplo de uso:
      # Insira o caminho para o seu arquivo CSV aqui
    dados = Deslizante.csv_para_lista_de_listas("deslizante.csv")
    print(dados)
    estado_inicial = Deslizante('', dados, (2,0), 0)
    algorithm = AEstrela()
    ts = time.time()
    result = algorithm.search(estado_inicial, trace=True)
    tf = time.time()
    if result != None:
        print('Achou!')
        print(result.show_path())
        print(f'Custo: {result.g}')
        print(f'Tempo: {tf-ts}')
    else:
        print('Nao achou solucao')

if __name__ == '__main__':
    main()