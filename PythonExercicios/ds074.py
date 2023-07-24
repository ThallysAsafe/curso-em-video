from random import randint
n = (randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10))
print(f'Os valores sorteados foram: ', end='')
print(f'{n}', end='')
print(f'\nO maior numero é: {max(n)}')
print(f'O menor numero é: {min(n)}')
