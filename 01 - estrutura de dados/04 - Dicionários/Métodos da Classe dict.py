# Usando métodos em dicionários

contatos = {
    "guilherme@gmail.com": {"nome": "Guilherme", "telefone": "3333-2221"},
    "giovanna@gmail.com": {"nome": "Giovanna", "telefone": "3443-2121"},
    "chappie@gmail.com": {"nome": "Chappie", "telefone": "3344-9871"},
    "melaine@gmail.com": {"nome": "Melaine", "telefone": "3333-7766"},
}

# Acessar telefone
print(contatos["giovanna@gmail.com"]["telefone"])  # "3443-2121"

# Copy
copia = contatos.copy()
copia["guilherme@gmail.com"] = {"nome": "Gui"}  # Atualiza o nome
print(contatos["guilherme@gmail.com"])  # {'nome': 'Guilherme', 'telefone': '3333-2221'}
print(copia["guilherme@gmail.com"])     # {'nome': 'Gui'}

# Fromkeys
dict.fromkeys(["nome", "telefone"])
dict.fromkeys(["nome", "telefone"], "vazio")

# Get
print(contatos.get("chave"))
print(contatos.get("chave", {}))
print(contatos.get("guilherme@gmail.com", {}))

# Items
print(contatos.items())

# Keys
print(contatos.keys())

# Setdefault
contatos.setdefault("nome", "Giovanna")
print(contatos)

# Update
contatos.update({"guilherme@gmail.com": {"nome": "Gui"}})
print(contatos)

# Pop
contatos.pop("melaine@gmail.com", "não encontrou!")
print(contatos)

# Popitem
contatos.popitem()
print(contatos)

# Values
print(contatos.values())

# In
print("chappie@gmail.com" in contatos)
print("idade" in contatos["chappie@gmail.com"])

# Del
del contatos["chappie@gmail.com"]
print(contatos)

# Clear
contatos.clear()
print(contatos)  # {}

