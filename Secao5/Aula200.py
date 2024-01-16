class Carro:
    def __init__(self, nome=''):
        self.nome = nome

    def acelerar(self):
        print(f'{self.nome} está acelerando...')



fusca = Carro()
fusca.nome = 'Fusca'
print(fusca.nome)

print()

celta = Carro(nome='Celta')
print(celta.nome)
celta.acelerar()
