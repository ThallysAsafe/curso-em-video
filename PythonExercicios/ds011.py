l = float(input('Quantos metros tem de largura a parede? '))
h = float(input('e quantos metros tem de altura a parede? '))
area = h * l
qt = area/2
print('Sua parede tem a dimensão de {}x{} e sua área é de {}m.'.format(l, h, area))
print('Para pintar essa parede, você precisará de {} litros de tinta.'.format(qt))
