from veiculo import Veiculo

class Moto(Veiculo):
    def __init__(self, marca, modelo, tipo) -> None:
        super().__init__(marca, modelo)
        self.tipo = tipo
    
    def __str__(self) -> str:
        info_pai =  super().__str__()
        return f'{info_pai} | {self.tipo}'
    
    def ligar(self):
        self._ligado= not self._ligado