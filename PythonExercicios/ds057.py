sexo = ''
while sexo != 'F' and sexo != 'M':
    sexo = str(input('Digite qual é o seu sexo: [M/F]')).upper()
    if sexo != 'F' and sexo != 'M':
        print('Porfavor, Digite Novamente!')
print('Fim')
