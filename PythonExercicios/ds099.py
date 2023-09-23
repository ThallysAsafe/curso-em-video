def maior(*num):
    print('-='*30)
    cont = maior = 0
    print('Analisando os valores passados...')
    for i in num:
        print(i, end=' ')
        if cont == 0:
            maior = i
        else:
            if i > maior:
                maior = i
        cont += 1
    print(f'Foram informados {len(num)} valores ao todo.')
    print(f'O maior valor informado foi {maior}.')

help(maior)