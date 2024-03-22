from aigyminsper.search.SearchAlgorithms import BuscaLargura, BuscaProfundidade, BuscaCustoUniforme, BuscaProfundidadeIterativa, AEstrela
from aigyminsper.search.Graph import State
import json
import time
import math


class Conjectura(State):

    def __init__(self, op, numero, quatro,flag_arrendondou, cost):
        # You must use this name for the operator!
        self.operator = op
        self.quatro = quatro
        self.numero = numero
        self.cost_ = cost
        self.flag_arredondou = flag_arrendondou

 

    def successors(self):
        
        successors = []
        if self.quatro < 100:
            successors.append(Conjectura("fatorial", self.numero, math.factorial(int(self.quatro)), self.flag_arredondou, 1))
        if (self.quatro)**0.5 > self.numero:
            successors.append(Conjectura("raiz", self.numero, (self.quatro)**0.5, self.flag_arredondou, 1))
        successors.append(Conjectura("arredonda", self.numero, math.floor(self.quatro), self.flag_arredondou, 1))

            
        
        # if self.quatro != math.floor(self.quatro):
            
        return successors
    
    def is_goal(self):
        return self.quatro == self.numero
    
    def description(self):
        return 'Problema do Conjectura'
    
    def cost(self):
        
        
        return self.cost_
    
    def h(self):
        return abs(self.numero) - abs(self.quatro)
    
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

def main():

    

# Exemplo de uso:
      # Insira o caminho para o seu arquivo CSV aqui

    estado_inicial = Conjectura('', 5, 4, True, 0)
    algorithm = BuscaProfundidadeIterativa()
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