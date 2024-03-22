import io
from contextlib import redirect_stdout


MUD = '■'
END = '⚑'


def cria_mapa(linhas, colunas, obstaculos, end):
    mapa = []
    for i in range(linhas):
        linha = []
        for j in range(colunas):
            linha.append('⛶')
        mapa.append(linha)
    for obstaculo in obstaculos:
        mapa[obstaculo[0]][obstaculo[1]] = MUD
    mapa[end[0]][end[1]] = END
    return mapa

direcao = ['l','r','u','d']
estado = 2
res = direcao[estado%4]

def imprime_mapa(mapa):
    with io.StringIO() as buf, redirect_stdout(buf):
        print('  ', end='')
        for n in range(len(mapa[0])):
            print(n, end=' ')
        print()
        for i, linha in enumerate(mapa):
            print(i, end=' ')
            print(' '.join(linha))
        return buf.getvalue()