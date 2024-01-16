import os
compras=list()
while True:
    print('Selecione uma opção')
    digitacao=str(input('[i]nserir [a]pagar [l]istar: '))
    try:
        if digitacao=='i':
            os.system('cls')
            compras.append(input('Item:'))
        elif digitacao=='a':
            indice=int(input('Escolha o índice para apagar: '))
            compras.pop(indice)
        elif digitacao=='l':
            os.system('cls')
            if len(compras)==0:
                print('Não há nada para listar')
            for i, valor in enumerate(compras):
                print(i, valor)
    except IndexError:
        print('Por favor, digite um índice existente')
        continue
    except ValueError:
        print('Por favor, digite um valor válido')