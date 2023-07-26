matriz = [[0, 0, 0],[0, 0, 0],[0, 0, 0]]
for l in range(0,3):
    for c in range(0, 3):
        matriz[l][c] = int(input(f'Digite um valor para [{l},{c}]: '))
for l in range(0, 3):
    for c in range(0,3):
        print(f'[{matriz[l][c]}]', end='')
    print()
soma = 0
for l in range(0, 3):
    for c in range(0, 3):
        if matriz[l][c] % 2 == 0:
            soma += matriz[l][c]
print(f'A soma dos valores da pares é: {soma}')
soma = 0
for l in range(0, 3):
    for c in range(2, 3):
        soma += matriz[l][c]
print(f'A soma dos valores da terceira coluna é: {soma}')
soma = 0
mai = 0
for l in range(1, 2):
    for c in range(0, 3):
        if c == 1:
            mai = matriz[l][c]
        if matriz[l][c] > mai:
            mai = matriz[l][c]
print(f'O maior numero da 2ª linha é: {mai}')

