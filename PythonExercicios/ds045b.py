import time
from random import randint
itens = ['Pedra', 'Papel', 'Tesoura']
computador = randint(0, 2)
print('''Suas opções:
[ 0 ] - Pedra 
[ 1 ] - Papel
[ 2 ] - Tesoura''')
jogador = int(input('Qual é a sua jogada? '))
print('JO')
time.sleep(0.5)
print('KEN')
time.sleep(0.5)
print('PÔ!')
time.sleep(0.5)
print('-=-' * 10)
print('O Computador jogou {}'.format(itens[computador]))
print('O Jogador jogou {}'.format(itens[jogador]))
print('-=-' * 10)
if computador == 0:
    if jogador == 0:
        print('EMPATE')
    elif jogador == 1:
        print('JOGADOR VENCE')
    elif jogador == 2:
        print('COMPUTADOR VENCE')
    else:
        print('JOGADA INVALIDA')
elif computador == 1:
    if jogador == 0:
        print('COMPUTADOR VENCE')
    elif jogador == 1:
        print('EMPATE')
    elif jogador == 2:
        print('JOGADOR VENCE')
    else:
        print('JOGADA INVALIDA')
elif computador == 2:
    if jogador == 0:
        print('JOGADOR VENCE')
    elif jogador == 1:
        print('COMPUTADOR VENCE')
    elif jogador == 2:
        print('EMPATE')
    else:
        print('JOGADA INVALIDA')
else:
    print('Erro')