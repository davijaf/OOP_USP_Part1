class Carro:
    def __init__(self, modelo, ano, cor):
        self.modelo = modelo
        self.ano = ano
        self.cor = cor

carro_terceiro = Carro("Ferrari", 1980, "Vermelha")

print(carro_terceiro.ano)
print(carro_terceiro.modelo)
print(carro_terceiro.cor)