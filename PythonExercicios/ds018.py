import math
ang = int(input('Digite o valor do angulo: '))
sen = math.sin(math.radians(ang))
cos = math.cos(math.radians(ang))
tan = math.tan(math.radians(ang))
print('O Angulo de {} tem o seno de {:.2f}'.format(ang, sen))
print('O Angulo de {} tem o cosseno de {:.2f}'.format(ang, cos))
print('O Angulo de {} tem a tangente de {:.2f}' .format(ang, tan))

