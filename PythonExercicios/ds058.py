from random import randint
print('===' * 10)
print('Joginho da Adivinhação')
print('===' * 10)
comp = randint(0, 10)
print('Adivinhe um numero de 0 a 10, a qual eu pensei!')
jogador = -1
p = 0
while jogador != comp:
    jogador = int(input('Digite o numero aqui: '))
    if jogador != comp:
        print('Errou tente novamente!')
        p += 1
print('Parabéns você acertou, eu pensei no numero {}, mas vc precisou de {} tentativas!'.format(comp, p))
