r1 = float(input('Digite o comprimento da primeira reta: '))
r2 = float(input('Digite o comprimento da segunda reta: '))
r3 = float(input('Digite o comprimento da terceira reta: '))
if(r1 + r2) > r3 and r1 + r3 > r2 and r2 + r3 > r1:
    print('Essas retas são capazes de formar um triangulo')
else:
    print('Essas retas não são capazes de formar um triangulo')
