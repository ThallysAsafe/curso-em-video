numeros = list()
while True:
    num = (int(input('Digite um valor: ')))
    if num not in numeros:
        numeros.append(num)
    else:
        print('Valor dupplicado, não será adicionado a lista')
    pergunta = str(input('Quer Continuar? [S/N] ')).upper()
    if pergunta in 'N':
        break
    elif pergunta != 'S':
        while True:
            print('Resposta inválida, Tente Novamente. ', end='')
            pergunta = str(input('Quer Continuar? [S/N] ')).upper().strip()
            if pergunta in 'SN':
                break
numeros.sort()
print(numeros)
