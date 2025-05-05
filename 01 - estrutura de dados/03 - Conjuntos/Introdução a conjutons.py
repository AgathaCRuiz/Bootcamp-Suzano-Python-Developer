# Conjuntos - Coleção que não possui objetos repetidos

set([1, 2, 3, 1, 3, 4])
set("abacaxi")
set(("palio", "gol", "celta", "palio"))

linguagens = {"python", "java", "python"}
print(linguagens)

# Conversão
numeros = {1, 2, 3, 2}
numeros = list(numeros)
print(numeros[0])

# Iterar + iteração com enumerate
carros = {"gol", "celta", "plaio"}
for carro in carros:
    print(carro)

for indice, carro in enumerate(carros):
    print(f"{indice}: {carro}")