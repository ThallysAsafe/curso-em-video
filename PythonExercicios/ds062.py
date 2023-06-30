print('Calculadora de PA')
a1 = float(input('Digite o primeiro termo da PA: '))
r = float(input('Digite a razão da PA: '))
v = a1
c = 0
s = ' '
print('Esses são os 10 primeiros termos:')
while c != 10 or s == 'S':
    if c == 0:
        v = v
        c += 1
    else:
        c += 1
        v += r
    print(v, end=' ')
s = str(input('Você deseja continuar? [S/N]')).upper()
print('Fim do programa')
