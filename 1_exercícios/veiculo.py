class Veiculo:
    veiculos = []
    
    def __init__(self, marca, modelo) -> None:
        self.marca = marca
        self.modelo = modelo
        self._ligado = False
        Veiculo.veiculos.append(self)
    
    @property
    def ligado(self):
        return 'ligado' if self._ligado else 'desligado'
    
    def __str__(self) -> str:
        return f'{self.marca} | {self.modelo} | {self.ligado}'
    
    @classmethod
    def listar_veiculos(self):
        print(f'{'Marca'.ljust(25)} | {'Modelo'.ljust(25)}')
        for veiculo in Veiculo.veiculos:
            print(f'{veiculo.marca.ljust(25)} | {veiculo.modelo.ljust(25)}')
    

if __name__ == '__main__':
    veiculo1 = Veiculo('Honda', 'Fit')
    print(veiculo1)
    Veiculo.listar_veiculos()