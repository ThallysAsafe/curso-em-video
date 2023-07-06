soma = 0
cont = 0
while True:
    num = int(input('Digite um valor: [999 para encerrar] '))
    if num != 999:
        cont += 1
        soma += num
    else:
        break
print(f'A soma dos {cont} valores digitados é igual a {soma}')
print('Programa Encerrado')
    