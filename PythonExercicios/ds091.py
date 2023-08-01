from random import randint
from time import sleep
from operator import itemgetter
jogo = {'jogador1': randint(1, 6),
        'jogador2': randint(1, 6),
        'jogador3': randint(1, 6),
        'jogador4': randint(1, 6)}
ranking = list()
print('Valores Sorteados')
for k, v in jogo.items():
    print(f'O {k} tirou {v}')
    sleep(0.5)
ranking = sorted(jogo.items(), key=itemgetter(1), reverse=True)
print('Ranking da Maior Pontuação')
for k, v in enumerate(ranking):
    print(f'{k+1}ºLugar: {v[0]} tirou {v[1]}')

