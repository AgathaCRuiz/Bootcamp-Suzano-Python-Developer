# Tuplas - são imutáveis
frutas = ("laranja", "pera", "uva", )
letras = tuple("python")
numeros = tuple([1, 2, 3, 4])
pais = ("Brasil", )

print(frutas[0], frutas[-1])

# Tuplas aninhadas - estruturas bidimensionais
matriz = (
    (1, "a", 2),
    ("b", 3, 4),
    (5, 6, "c"),
)

print(matriz[0], matriz[0][0])

# Fatiamento
tupla = ("p", "y", "t", "h", "o", "n", )

print("\n", tupla[2:], "\n", tupla[:2], "\n", tupla[::], "\n")

# Iteração
carros = ("gol", "celta", "palio", )
for carro in carros:
    print(carro)

for indice, carro in enumerate(carros):
    print(f"{indice}: {carro}")

# Métodos em Tuplas
cores = ("vermelho", "azul", "verde", "azul", )
print(cores.count("azul")) #count
print(cores.index("azul")) #index
print(len(cores)) #len