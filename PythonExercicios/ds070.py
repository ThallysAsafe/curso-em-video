print('-'*20)
print('SuperMercado')
print('-'*20)
cont = 0
x = 1
barato = ''
vt = 0
menor = 0
pergunta = ''
while True:
    nome = str(input('Nome do Produto: '))
    preço = float(input('Preço desse Produto: '))
    pergunta = str(input('Mais Alguma Coisa? [S/N]')).upper().strip()
    vt += preço
    if x == 1:
        menor = preço
        barato = nome
        x += 1
        if preço > 1000:
            cont += 1
    elif x > 1:
        if menor > preço:
            menor = preço
            barato = nome

            if preço > 1000:
                cont += 1
        cont += 1
    if pergunta == 'N':
        break
    print('-'*20)
print('Finalizando Compra')
print('-=-'*20)
print(f'O total Gasto na Compra foi de R$ {vt}')
print(f'{cont} Produtos custam mais de R$1000')
print(f'O Produto mais barato foi {barato}')
print('-=-' * 20)
