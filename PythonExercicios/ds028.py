from random import randint
from time import sleep
print('-=-' * 20)
print('Adivinhe um numero de 0 a 5, que eu pensei!')
print('-=-' * 20)
num = int(input('digite o numero que vc acha que eu escolhi: '))  # O que o Jogador acha!
n = randint(0, 5)  # O que o computador pensou!
print('PROCESSANDO....')
sleep(2)
if num == n:
    print('Parabéns você acertou!!')
else:
    print('Você perdeu! haahaha pensei no numero {}, e não no numero {}'.format(n, num))
