v = float(input('Qual o valor do produto? R$'))
av = v - (v * 10/100)
ca = v + (v * 8/100)
print('O valor do produto era {}, e o valor dele avista é de {} e no cartão {}'.format(v, av, ca))