from random import randint
from time import sleep
print('='*30)
print(f'{"Jogo da Mega Sena":^30}')
print('='*30)
qtd = int(input('Quantos Jogos quer que eu sorteie? '))
print('-='*20, f'{"SORTEANDO":^10}', f'{{qtd}}', f'{"JOGOS":^20}')
for i in range(0, qtd):
    num = [randint(1, 60), randint(1, 60), randint(1, 60), randint(1, 60), randint(1, 60), randint(1, 60)]
    print(f'Jogo {i+1}: {num}')
    sleep(0.5)
print('-='*20, f'{"< BOA SORTE! >":^20}')
