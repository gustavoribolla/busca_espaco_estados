from aigyminsper.search.SearchAlgorithms import BuscaLargura, BuscaProfundidade, BuscaCustoUniforme, BuscaProfundidadeIterativa, BuscaGananciosa, AEstrela
from aigyminsper.search.Graph import State
import json
import time
import copy
import math
import csv


class Rainhas(State):
    @staticmethod
    def diagonais_do_ponto(mapa, linha, coluna):
        diagonais = []

        # Adiciona o valor do ponto atual à lista de diagonais
        diagonais.append(mapa[linha][coluna])

        # Movimento diagonal para cima e para a esquerda
        i, j = linha - 1, coluna - 1
        while i >= 0 and j >= 0:
            diagonais.append(mapa[i][j])
            i -= 1
            j -= 1

        # Movimento diagonal para cima e para a direita
        i, j = linha - 1, coluna + 1
        while i >= 0 and j < len(mapa[0]):
            diagonais.append(mapa[i][j])
            i -= 1
            j += 1

        # Movimento diagonal para baixo e para a esquerda
        i, j = linha + 1, coluna - 1
        while i < len(mapa) and j >= 0:
            diagonais.append(mapa[i][j])
            i += 1
            j -= 1

        # Movimento diagonal para baixo e para a direita
        i, j = linha + 1, coluna + 1
        while i < len(mapa) and j < len(mapa[0]):
            diagonais.append(mapa[i][j])
            i += 1
            j += 1

        return diagonais

    @staticmethod
    def csv_para_lista_de_listas(arquivo_csv):
        lista_de_listas = []
        with open(arquivo_csv, newline='') as csvfile:
            leitor = csv.reader(csvfile, delimiter=',')
            for linha in leitor:
                lista_de_inteiros = [int(valor) for valor in linha]
                lista_de_listas.append(lista_de_inteiros)
        return lista_de_listas

    def __init__(self, op, mapa, cost):
        # You must use this name for the operator!
        self.operator = op
        self.mapa = mapa
        self.cost_ = cost
   
 
    def successors(self):
        
        successors = []
    
        colunas = []

        for x in range(len(self.mapa[0])):
            new = []
            for y in range(len(self.mapa)):
                new.append(self.mapa[y][x])
            colunas.append(new)
        
        for x in range(len(self.mapa)):
            for y in range(len(self.mapa[0])):
                lista_diagonais = Rainhas.diagonais_do_ponto(self.mapa, x, y)
                if not(1 in lista_diagonais or 1 in colunas[y] or 1 in self.mapa[x]):
                    mapa_novo = copy.deepcopy(self.mapa)
                    mapa_novo[x][y] = 1
                    successors.append(Rainhas(f"Rainha em {x},{y}", mapa_novo, 1))  
        return successors
    
    def is_goal(self):
        contador = 0
        for i in range(len(self.mapa)):
            for j in range(len(self.mapa[i])):
                if self.mapa[i][j]  == 1:
                    contador += 1
        
        return contador == 8
    
    def description(self):
        return 'Problema do Rainhas'
    
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
    dados = Rainhas.csv_para_lista_de_listas("rainhas.csv")
    print(dados)
    estado_inicial = Rainhas('', dados, 0)
    algorithm = BuscaProfundidade()
    ts = time.time()
    result = algorithm.search(estado_inicial, trace=True, m=10)
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