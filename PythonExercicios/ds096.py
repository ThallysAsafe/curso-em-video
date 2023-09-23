print('Controle de Terrenos')
print('--------------------')
largura = float(input('Largura (m): '))
comprimento = float(input('Comprimento (m): '))
def area(largura,comprimento):
    print(f'A área de um terreno {largura}x{comprimento} é de {largura*comprimento:2f}m²')
area(largura,comprimento)