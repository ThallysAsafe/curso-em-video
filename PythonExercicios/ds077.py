palavras = ('aprender', 'programar', 'linguagem', 'python'
            'curso', 'gratis', 'estudar', 'praticar', 'trabalhar',
            'mercado', 'programador', 'futuro')
for c in palavras:
    print(f'\nNa palavra {c} temos as vogais: ', end='')
    for letra in c:
        if letra.lower() in 'aeiou':
            print(f'{letra}', end=' ')
