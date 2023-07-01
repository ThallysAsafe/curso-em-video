print('Calculadora de PA')
a1 = float(input('Digite o primeiro termo da PA: '))
r = float(input('Digite a razão da PA: '))
v = a1
s = ' '
n = 10
print('Esses são os 10 primeiros termos:')
while s != 'N':
    x = 0
    while x != n:
        print(v, end=' ')
        v += r
        x += 1
    s = str(input('\nVocê deseja continuar? [S/N]')).upper()
    n = int(input('Quantos termos você quer adicionar: '))
    if n == 0:
        s = 'N'
print('Fim do programa')
