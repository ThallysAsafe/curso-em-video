import random
def sorteio():
    numeros = []
    print('Sorteando 5 valores da lista:', end=' ')
    for i in range(0,5):
        num = random.randint(1,10)
        print(num,end=' ')
        numeros.append(num)
    print('PRONTO!')
    return somaPar(numeros)
def somaPar(numeros):
    soma = 0
    for i in numeros:
        if i % 2 == 0:
            soma += i
    print(f'Somando os valores pares de {numeros}, temos {soma}')
sorteio()