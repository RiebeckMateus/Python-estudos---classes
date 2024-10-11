from item_cardapio import ItemCardapio

class Sobremesa(ItemCardapio):
    def __init__(self, nome, preco, tipo, tamanho, descricao):
        super().__init__(nome, preco)
        self.tipo = tipo
        self.tamanho = tamanho
        self.descricao = descricao
    
    def __str__(self) -> str:
        info_pai = super().__str__()
        return f'{info_pai} | {self.tipo} | {self.tamanho} | {self.descricao}'
    
    def aplicar_desconto(self, desconto):
        self._preco -= (self._preco * desconto)
        
if __name__ == '__main__':
    sobremesa1 = Sobremesa('Haggandars', 70, 'Sorvete', 'Pequeno', 'Sorvete incrivelmente bom... que eu nunca comi')
    sobremesa1.aplicar_desconto(.5)
    print(sobremesa1)