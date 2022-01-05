class Carro:
    def __init__(self) -> None:
        self.cor = None
        self.modelo = None
        self.fabricante = None

    def acelerar(self):
        print('estou acelerando nesse {} de cor {}'.format(self.modelo, self.cor))

    def __str__(self) -> str:
        return 'carro {} {} de cor {}'.format(self.fabricante, self.modelo, self.cor)


carro1 = Carro()
carro1.fabricante = 'Ford'
carro1.modelo = 'Ka'
carro1.cor = 'Vermelho'

print(carro1)
