from time import sleep
n = int(input('Digite um primeiro termo para calcular uma P.A: '))
r = int(input('Digite sua razão: '))
c = n
total = 0
cont = 1
mais = 10
while mais != 0:
    total += mais
    print('Calculando P.A')
    while cont <= total:
        print('{}, '.format(c), end='')
        cont += 1
        c += r
    mais = int(input('\nQuantos termos deseja adicionar a mais: '))
print('Finalizando Programa!')
sleep(1)
print('Fim')


