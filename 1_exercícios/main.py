from carro import Carro
from moto import Moto

carro_honda_fit = Carro('Honda', 'Fit', 4, 'Grafite')
carro_honda_civic = Carro('Honda', 'Civic', 4, 'Preto')
carro_fiat_uno = Carro('Fiat', 'Uno', 2, 'Cinza')

moto_honda_bis = Moto('Honda', 'Bis', 'Casual')
moto_yamaha_fazer = Moto('Yamaha', 'Fazer', 'Casual')
moto_kawasaki_ninja = Moto('Kawasaki', 'Ninja', 'Casual')

carro_honda_fit.ligar()

print(carro_honda_fit)
print(carro_honda_civic)
print(carro_fiat_uno)
print(moto_honda_bis)
print(moto_yamaha_fazer)
print(moto_kawasaki_ninja)