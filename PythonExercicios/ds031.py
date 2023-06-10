d = float(input('Qual é a distancia em km da sua viagem? '))
if d <= 200:
    print('O valor de sua passagem é de {:.2f} R$'.format(d * 0.5))
else:
    print('O valor de sua passagem é de {:.2f} R$'.format(d * 0.45))