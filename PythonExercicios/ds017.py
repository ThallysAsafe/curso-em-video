from math import sqrt
print('=='*12)
print('Calculadora de Hiportenusa')
co = float(input('Digite o valor do Cateto Oposto: '))
ca = float(input('Digite o valor do Cateto Adjacente: '))
h = sqrt(co ** 2 + ca ** 2)
print('O valor da Hiportenusa é {:.2f}'.format(h))
print('=='*12)
