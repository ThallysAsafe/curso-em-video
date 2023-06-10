n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
m = (n1 + n2)/2
if m>=6:
    print('Parabéns! você passou de ano! com a media: {}'.format(m))
else:
    print('Você foi de vasco amigo! ou melhor reprovado')