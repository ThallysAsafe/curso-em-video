op = 0
while op != 5:
    n1 = float(input('Digite o primeiro número: '))
    n2 = float(input('Digite o segundo número: '))
    op = int(input('''[MENU]
[1]-Somar
[2]-Multiplicar
[3]-Maior
[4]-Novos Numeros
[5]-Sair do Programa
Digite sua opção: '''))
    if op == 1:
        n3 = n1 + n2
        print('O valor da soma de {} + {} = {}'.format(n1, n2, n3))
    elif op == 2:
        n3 = n1 * n2
        print('O valor da multiplicação de {} x {} = {}'.format(n1, n2, n3))
    elif op == 3:
        if n1 > n2:
            print('O Maior Número é {}'.format(n1))
        elif n1 == n2:
            print('Os Números são iguais, logo o maior número {}!'.format(n1))
        else:
            print('O Maior Número é {}'.format(n2))
print('Fim do programa!')
