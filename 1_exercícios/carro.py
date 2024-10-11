from veiculo import Veiculo

class Carro(Veiculo):
    def __init__(self, marca, modelo, portas, cor) -> None:
        super().__init__(marca, modelo)
        self.portas = portas
    
    def __str__(self) -> str:
        info_pai = super().__str__()
        return f'{info_pai} | {self.portas} portas'
    
    def ligar(self):
        self._ligado= not self._ligado

if __name__ == '__main__':
    carro1 = Carro('Honda', 'Fit', '4')
    carro1.ligar()
    carro1.ligar()
    print(carro1)