d = float(input('Qual é a distancia em km da sua viagem? '))
if d <= 200:
    print('O valor de sua passagem é de \033[1;32;40m{:.2f} R$\033[m '.format(d * 0.5))
else:
    print('O valor de sua passagem é de \033[1;32;40m{:.2f} R$\033[m '.format(d * 0.45))