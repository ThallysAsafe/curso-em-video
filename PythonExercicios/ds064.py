x = 0
z = 0
c = 0
while c != 999:
    c = int(input('Digite um número inteiro[999 para parar o programa]: '))
    if c != 999:
        x += c
        z += 1
print('Foram digitados {} numeros! e a soma de todos eles, exceto o 999 é {}'.format(z, x))
