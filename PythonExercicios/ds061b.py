print('-=-' * 10)
print('CALCULADORA DE P.A')
print('-=-' * 10)
primeiro = int(input('Digite o Primeiro Termo: '))
razão = int(input('Digite o segundo termo: '))
termo = primeiro
cont = 1
while cont <= 10:
    print('{}, '.format(termo), end=' ')
    termo += razão
    cont += 1
print('Fim do programa!')