print('Tabuada Versão 3.0')
print('-=-'*20)
v = 0
num = int(input('Digite um numero para mostrar a tabuada do mesmo: '))
while True:
    v = 0
    if num >= 0:
        while v != 10:
            v += 1
            m = v * num
            print(f'{num} x {v} = {m}')
    else:
        break
    print('-'*20)
    num = int(input('Digite um numero para mostrar a tabuada do mesmo: '))
    print('-' * 20)
print('Programa Tabuada Encerrado, Volte Sempre!')
