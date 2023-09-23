a = 'Olá, mundo'
def escreva(a = 'Olá, mundo'):
    print('~'*(len(a)+2))
    m = len(a)
    print(f'{a:^{(m)+2}}')
    print('~'*(len(a)+2))
escreva(a)