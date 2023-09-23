# Faça um programa que tenha uma função chamada contador(), que receba três parâmetros: início, fim e passo. Seu programa tem que realizar três contagens através da função criada:                                                                                              
#a) de 1 até 10, de 1 em 1                                                
#b) de 10 até 0, de 2 em 2
# c) uma contagem personalizada
def contagem():
    print('-='*20)
    print('Contagem de 1 até 10 de 1 em 1')
    for i in range(1,10+1,1):
        print(i,end=' ')
    print('FIM!')
    print('-='*20)
    print('Contagem de 10 até 0 de 2 em 2')
    for i in range(10,0-1,-2):
        print(i,end=' ')
    print('FIM!')
    print('-='*20)
    print('Agora é sua vez de personalizar a contagem!')
    ini = int(input('Início: '))
    fim = int(input('Fim: '))
    passo = int(input('Passo: '))
    print('-='*20)
    if ini > fim:
        if passo < 0:
            print(f'Contagem de {ini} até {fim} de {passo*-1} em {passo*-1}')
            for i in range(ini,fim-1,passo):
                print(i,end=' ')
            print('FIM!')
        elif passo == 0:
            print(f'Contagem de {ini} até {fim} de {1} em {1}')
            for i in range(ini,fim-1,-1):
                print(i,end=' ')
            print('FIM!')
        else: 
            print(f'Contagem de {ini} até {fim} de {passo} em {passo}')
            for i in range(ini,fim-1,passo*-1):
                print(i,end=' ')
            print('FIM!')
    else:
        if passo < 0:
            print(f'Contagem de {ini} até {fim} de {passo*-1} em {passo*-1}')
            for i in range(ini,fim+1,passo*-1):
                print(i,end=' ')
            print('FIM!')
        elif passo == 0:
            print(f'Contagem de {ini} até {fim} de {1} em {1}')
            for i in range(ini,fim+1,1):
                print(i,end=' ')
            print('FIM!')
        else: 
            print(f'Contagem de {ini} até {fim} de {passo} em {passo}')
            for i in range(ini,fim+1,passo):
                print(i,end=' ')
            print('FIM!')
contagem()