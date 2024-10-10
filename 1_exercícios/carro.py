from veiculo import Veiculo

class Carro(Veiculo):
    def __init__(self, marca, modelo, portas) -> None:
        super().__init__(marca, modelo)
        self.portas = portas
    
    def __str__(self) -> str:
        info_pai = super().__str__()
        return f'{info_pai} | {self.portas} portas'

if __name__ == '__main__':
    carro1 = Carro('Honda', 'Fit', '4')
    print(carro1)