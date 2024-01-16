def criar_multiplicador(multiplicador):
    def multiplicar(numero):
        return numero * multiplicador
    return multiplicar


duplicar=criar_multiplicador(2)
triplicar=criar_multiplicador(3)
quadruplicar=criar_multiplicador(4)

print(f'o dobro de 5 é:{duplicar(5)}')
print(f'o triplo de 5 é:{triplicar(5)}')
print(f'o quadruplo de 5 é:{quadruplicar(5)}')
