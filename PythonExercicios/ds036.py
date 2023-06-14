vc = float(input('Qual é o valor da casa? '))
sc = float(input('Quanto é o seu salário? '))
anos = int(input('Quantos anos vc deseja quitar? '))
mes = anos * 12
pm = vc / mes
if pm <= (30/100 * sc):
    print('Para pagar a casa de {} R$ em {} anos a prestações será de {:.2f} R$!'.format(vc, anos, pm))
    print('Empréstimo CONCEDIDO')
elif pm > (30/100 * sc):
    print('Para pagar a casa de {} R$ em {} anos a prestações será de {:.2f} R$!'.format(vc, anos, pm))
    print('Empréstimo NEGADO')
