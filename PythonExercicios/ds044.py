preco = float(input('Digite o valor do produto: '))
cond = str(input('Escolha a forma de pagamento: '))
cond = cond.upper()
if cond == 'DINHEIRO' or cond == 'CHEQUE':
    v = preco - (preco * 10/100)
    print('O valor total do produto será {} R$, com o pagamento em dinheiro ou cheque fica por {} R$'.format(preco, v))
elif cond == 'CARTÃO A VISTA' or cond == 'CARTAO A VISTA':
    v = preco - (preco * 5/100)
    print('O valor total do produto será {} R$, com o pagamento no cartão a vista fica por {} R$'.format(preco, v))
elif cond == 'CARTÃO PARCELADO' or cond == 'CARTAO PARCELADO':
    pac = float(input('Caso você queira parcelar, digite a quantidades de vezes: '))
    if pac == 2:
        pre2 = preco / pac
        print('O valor total do produto será {} R$, divido em {} parcelas de {} R$'.format(preco, pac, pre2))
    elif pac > 2:
        v = preco + (preco * 20/100)
        pre2 = v / pac
        print('O valor total do produto será {} R$, divido em {} parcelas de {} R$'.format(v, pac, pre2))
