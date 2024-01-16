class Camera:
    def __init__(self, nome, filmando=False, fotografando=False):
        self.nome = nome
        self.filmando = filmando
        self.fotografando=fotografando

    def filmar(self):
        if self.fotografando:
            print(f'{self.nome} já está fotografando...')

        print(f'{self.nome} está filmando...')
        self.filmando = True

    def parar_filmar(self):
            if not self.fotografando:
                print(f'{self.nome} não está fotografando...')

            print(f'{self.nome} está parando de filmar...')
            self.filmando = False


    def fotografar(self):
        if self.filmando:
            print(f'{self.nome} Não há como fotopgrafar filmando')
            return
        print(f'{self.nome} está fotografando...')
        self.filmando = True

c1 = Camera('Canon')
c2 = Camera('Sony')

c1.filmar()
c1.filmar()
c1.fotografar()
c1.parar_filmar()
c1.fotografar()

print()

c2.fotografar()
c2.filmar()
c2.parar_filmar()
c2.filmar()
c2.fotografar()