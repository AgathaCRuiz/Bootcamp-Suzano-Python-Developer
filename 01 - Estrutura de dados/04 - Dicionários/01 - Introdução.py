# Dicionários - conjunto não-ordenado de pares chave:valor, 
# onde as chaves são únicas em um dada instância

pessoa = {"nome": "Guilerme", "Idade": 28}
pessoa = dict(nome="Guilerme", idade=28)
pessoa["telefone"] = "3333-1234"

# {"nome": "Guilerme", "idade": 28, "telefone": "3333-1234"}

print(pessoa)
print(pessoa["nome"])

# Dicionário Aninhado

contatos = {
    "guilherme@gmail.com": {"nome": "Guilherme", "telefone": "3333-2221"},
    "giovanna@gmail.com": {"nome": "Giovanna", "telefone": "3443-2121"},
    "chappie@gmail.com": {"nome": "Chappie", "telefone": "3344-9871"},
    "melaine@gmail.com": {"nome": "Melaine", "telefone": "3333-7766"},
}

print(contatos["giovanna@gmail.com"]["telefone"])  # "3443-2121"

# Iterando em Dicionários
for chave in contatos:
    print(chave, contatos[chave])

for chave, valor in contatos.items():
    print(chave, valor)