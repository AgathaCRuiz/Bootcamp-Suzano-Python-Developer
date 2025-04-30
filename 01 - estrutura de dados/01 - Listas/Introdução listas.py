frutas = ["laranja", "maçã", "uva", "pera"]
letras= list("python")
numeros = list(range(10))
carro = ["Ferrari", "F8", 4500, "São Paulo", True]

print("\n", frutas[0], "\n", frutas[2], "\n", frutas[-1])

frutas = []

print("\n", frutas,"\n", letras,"\n", numeros,"\n", carro)

# Lista aninhada - listas que armazenam outras listas

matriz = [
    [1, "a", 2],
    ["b", 3, 4],
    [6, 5, "c"]
]

print("\n", matriz[0],"\n", matriz[1])
print("\n", matriz[0][0], "\n", matriz[0][-1], "\n", matriz[-1][-1])

# Fatiamento
lista = ["p", "y", "t", "h", "o", "n"]

print("\n", lista[2:], "\n", lista[:2], "\n", lista[1:3])
print("\n", lista[0:3:2], "\n", lista[::], "\n", lista[::-1], "\n")


# Iterar
carros = ["gol", "celta", "palio"]

for carro in carros:
    print(carro)

# Enumarate
print("\n")
for indice, carro in enumerate(carros):
    print(f"{indice}: {carro}")

# List comprehension
numeros = [1, 30, 21, 2, 9, 65, 34]
pares = []

for numero in numeros:
    if numero % 2 ==0:
        pares.append(numero)

print("\n", pares)

pares = [numero for numero in numeros if numero % 2 == 0]
print("\n", pares)

quadrado = [numero ** 2 for numero in numeros]
print("\n", quadrado)