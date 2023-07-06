print('Sequencia de Fibonacci')
print('=-='*20)
quantidade = int(input('Digite quantos termos você quer mostrar? '))
print('=-='*20)
cont = 0
while cont <= quantidade:
    cont += 1
    if cont == 1:
        t1 = 0
        t2 = 1
        t3 = t2 + t1
        print('{} -> {} ->'.format(t1, t2), end=' ')
    else:
        t1 = t2
        t2 = t3
        t3 = t2 + t1
    print('{} ->'.format(t3), end=' ')
print('Fim!!!')
