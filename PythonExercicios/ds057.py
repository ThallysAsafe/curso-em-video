sexo = ''
sexo = str(input('Digite qual é o seu sexo: [M/F]')).upper().strip() [0]
while sexo not in 'MmFf':
        sexo = str(input('Dados Invalidos! Porfavor, Digite Novamente! ')).strip().upper()[0]
print('Sexo {} registrado com sucesso!'.format(sexo))
print('Fim')
