from random import randint
print('-=-' * 30)
print('VAMOS JOGAR PAR OU IMPÁR!')
print('-=-' * 30)
x = ' '
vitorias = 0
while True:
    num = int(input('Diga um numero: '))
    x = str(input('Par ou impar? [P/I]')).upper()
    comp = randint(0, 10)
    soma = comp + num
    if x == 'P':
        if soma % 2 == 0:
            print(f'Você Jogou {num} e o Computador Jogou {comp}')
            print(f'{soma} é Par')
            print('Parabéns, Você Venceu! Vamos Jogar Novamente!')
            vitorias += 1
        else:
            print(f'Você Jogou {num} e o Computador Jogou {comp}')
            print(f'{soma} é Impár')
            print('Infelizmente, Você Perdeu')
            if vitorias >= 1:
                print(f'GAME OVER!, Você venceu {vitorias} vezes')
            break
    if x == 'I':
        if soma % 2 != 0:
            print(f'Você Jogou {num} e o Computador Jogou {comp}')
            print(f'{soma} é Impár')
            print('Parabéns, Você Venceu! Vamos Jogar Novamente!')
            vitorias += 1
        else:
            print(f'Você Jogou {num} e o Computador Jogou {comp}')
            print(f'{soma} é Par')
            print('Infelizmente, Você Perdeu')
            if vitorias >= 1:
                print(f'GAME OVER!, Você venceu {vitorias} vezes')
            break
