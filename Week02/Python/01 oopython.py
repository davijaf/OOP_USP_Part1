class Carro:
    pass

meu_carro = Carro()

print(meu_carro)

meu_carro.ano = 1968
meu_carro.cor = "Fusca"
meu_carro.modelo = "Azul"

print(meu_carro.ano)

seu_carro = Carro()
seu_carro.ano = 1981
seu_carro.cor = "Brasília"
seu_carro.modelo = "Amarelo"
print(seu_carro.ano)

novofusca = meu_carro

novofusca.ano += 10

print(novofusca.ano)