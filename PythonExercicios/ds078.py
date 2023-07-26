listnum = []
menor = 0
maior = 0
for c in range(0,5):
    listnum.append(int(input(f'Digite um valor na posição {c}: ')))
    if c == 0:
        menor = maior = listnum[c]
    else:
        if listnum[c] >= maior:
            maior = listnum[c]
        else:
            menor = listnum[c]
print('='*30)
print(f'Voce digitou esses valores: {listnum}')
print(f'O maior valor foi {maior} na posição ', end='')
for i, v in enumerate(listnum):
    if v == maior:
        print(f'{i}...', end=' ')
print('')
print(f'O menor valor foi {menor} na posição ', end='')
for i, v in enumerate(listnum):
    if v == menor:
        print(f'{i}...', end=' ')

