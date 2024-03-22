from aigyminsper.search.SearchAlgorithms import BuscaProfundidadeIterativa
from aigyminsper.search.Graph import State
import time


class Queens(State):
    def __init__(self, board, queens, n):
        self.n = n
        self.board = [['⛶' for _ in range(8)] for _ in range(8)]
        self.queens = queens
        for queen in queens:
            self.board[queen[0]][queen[1]] = '♛'

    def being_attacked(self, queen):
        for q in self.queens:
            if q[0] == queen[0] or q[1] == queen[1] or abs(q[0] - queen[0]) == abs(q[1] - queen[1]):
                return True
        return False

    def successors(self):
        successors = []
        for line in range(8):
            pos_queen = (line, self.n)
            if not self.being_attacked(pos_queen):
                new_queens = self.queens.copy()
                new_queens.append(pos_queen)
                successors.append(Queens(self.board, new_queens, self.n+1))
        return successors

    def print_board(self):
        for row in self.board:
            print(' '.join(row))
        print()
        
    def env(self):
        return self.queens

    def is_goal(self):
        return len(self.queens) == 8
    
    def description(self):
        return "Fit 8 queens that don't threaten each other"
    
    def cost(self):
        return 1


def main():
    state = Queens([], [], 0)
    algorithm = BuscaProfundidadeIterativa()
    result = algorithm.search(state, trace=True)
    if result is not None:
        print("Solucao encontrada:")
        result.state.print_board()
        print(f"Custo: {result.g}")
    else:
        print("Nenhuma solucao encontrado")

if __name__ == "__main__":
    main()