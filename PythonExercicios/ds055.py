pesomaior = 0
pesomenor = 0
for c in range(1, 6):
    peso = float(input('Digite o peso da {}º pessoa em kg: '.format(c)))
    if c == 1:
        pesomaior = peso
        pesomenor = peso
    elif peso > pesomaior:
        if pesomaior <= pesomenor:
            pesomenor = pesomaior
        pesomaior = peso
print('O peso maior é {} Kg, e o peso menor é {} Kg'.format(pesomaior, pesomenor))
    