print('-'*20)
print('SuperMercado')
print('-'*20)
cont = 0
x = 1
barato = ' '
vt = 0
menor = 0
while True:
    nome = str(input('Nome do Produto: '))
    preço = float(input('Preço desse Produto: '))
    vt += preço
    if x == 1 or preço < menor:
        menor = preço
        barato = nome
        x += 1
    if preço > 1000:
        cont += 1
    pergunta = ' '
    while pergunta not in 'SN':
        pergunta = str(input('Mais Alguma Coisa? [S/N]')).upper().strip()[0]
    if pergunta == 'N':
        break
    print('-'*20)
print('Finalizando Compra')
print('-=-'*20)
print(f'O total Gasto na Compra foi de R$ {vt}')
print(f'{cont} Produtos custam mais de R$1000')
print(f'O Produto mais barato foi {barato} que custa {menor}')
print('-=-' * 20)
