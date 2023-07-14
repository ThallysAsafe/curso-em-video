from random import randint
print('-=-' * 30)
print('VAMOS JOGAR PAR OU IMPÁR!')
print('-=-' * 30)
x = ' '
vitorias = 0
while True:
    num = int(input('Diga um numero: '))
    while x not in 'PI':
        x = str(input('Par ou impar? [P/I]')).upper().strip()[0]
    comp = randint(0, 10)
    soma = comp + num
    if x == 'P':
        if soma % 2 == 0:
            print(f'Você Jogou {num} e o Computador Jogou {comp}, e o valor da soma {soma} é Par')
            print('Parabéns, Você Venceu! Vamos Jogar Novamente!')
            vitorias += 1
        else:
            print(f'Você Jogou {num} e o Computador Jogou {comp}, e o valor da soma {soma} é Impar')
            print('Infelizmente, Você Perdeu')
            if vitorias >= 1:
                print(f'GAME OVER!, Você venceu {vitorias} vezes')
            break
    if x == 'I':
        if soma % 2 != 0:
            print(f'Você Jogou {num} e o Computador Jogou {comp}, e o valor da soma {soma} é Impar')
            print('Parabéns, Você Venceu! Vamos Jogar Novamente!')
            vitorias += 1
        else:
            print(f'Você Jogou {num} e o Computador Jogou {comp}, e o valor da soma {soma} é Par')
            print('Infelizmente, Você Perdeu')
            if vitorias >= 1:
                print(f'GAME OVER!, Você venceu {vitorias} vezes')
            break
