import random
print('-=-'*20)
print('Vamos jogar Jokenpô!')
jogador = str(input('Escolha, pedra, papel e tesoura: '))
print('-=-'*20)
lista = ['PEDRA', 'PAPEL', 'TESOURA']
c = random.choice(lista)
jogador = jogador.upper()
if c == jogador:
    print('Empate, eu escolhi {} e você escolheu {}'.format(c, jogador))
elif jogador == 'PEDRA' and c == 'PAPEL':
    print('Eu ganhei, eu escolhi {} e você escolheu {}'.format(c, jogador))
elif jogador == 'PAPEL' and c == 'TESOURA':
    print('Eu ganhei, eu escolhi {} e você escolheu {}'.format(c, jogador))
elif jogador == 'TESOURA' and c == 'PEDRA':
    print('Eu ganhei, eu escolhi {} e você escolheu {}'.format(c, jogador))
elif jogador == 'PEDRA' and c == 'TESOURA':
    print('Você venceu, eu escolhi {} e você escolheu {}'.format(c, jogador))
elif jogador == 'TESOURA' and c == 'PAPEL':
    print('Você venceu, eu escolhi {} e você escolheu {}'.format(c, jogador))
elif jogador == 'PAPEL' and c == 'PEDRA':
    print('Você venceu, eu escolhi {} e você escolheu {}'.format(c, jogador))
