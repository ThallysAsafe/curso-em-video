print('-=-'*20)
print('Caixa Eletrônico')
print('-=-'*20)
saque = int(input('Digite o Valor em numeros inteiros que vc deseja sacar: '))
cont50 = cont20 = cont10 = cont1 = cont = 0
while True:
    if saque >= 50:
        saque -= 50
        cont50 += 1
        cont += 1
    elif saque >= 20:
        saque -= 20
        cont20 += 1
        cont += 1
    elif saque >= 10:
        saque -= 10
        cont10 += 1
        cont += 1
    elif saque >= 1:
        saque -= 1
        cont1 += 1
        cont += 1
    elif saque == 0:
        break
print(f'Total de {cont50} cédulas de R$50')
print(f'Total de {cont20} cédulas de R$20')
print(f'Total de {cont10} cédulas de R$10')
print(f'Total de {cont1} cédulas de R$1')
