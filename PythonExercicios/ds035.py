r1 = float(input('Digite o comprimento da primeira reta: '))
r2 = float(input('Digite o comprimento da segunda reta: '))
r3 = float(input('Digite o comprimento da terceira reta: '))
if(r1 + r2) > r3 > (r1 - r2) * -1:
    print('Essas retas são capazes de formar um triangulo')
else:
    print('Essas retas não são capazes de formar um triangulo')
