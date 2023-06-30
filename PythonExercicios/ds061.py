print('Calculadora de PA')
a1 = float(input('Digite o primeiro termo da PA: '))
r = float(input('Digite a razão da PA: '))
v = a1
c = 0
print('Esses são os 10 primeiros termos:')
while c != 10:
    if c == 0:
        v = v
        c += 1
    else:
        c += 1
        v += r
    print(v, end=' ')
print('Fim do programa')