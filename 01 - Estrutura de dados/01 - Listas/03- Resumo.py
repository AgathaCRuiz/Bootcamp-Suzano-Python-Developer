
# COLA DE MÉTODOS DA CLASSE list EM PYTHON 🐍

# Criando uma lista vazia
lista = []

# APPEND ➕
# Adiciona um item ao final da lista
lista.append(42)

# COPY 🧪
# Cria uma cópia da lista
copia = lista.copy()

# COUNT 🔢
# Conta quantas vezes um valor aparece na lista
lista.count(42)

# EXTEND 📚
# Adiciona vários elementos de outra lista
lista.extend([1, 2, 3])

# INDEX 🔍
# Retorna a posição do primeiro valor encontrado
lista.index(1)

# CLEAR 🧹
# Remove todos os elementos da lista
lista.clear()

# REVERSE 🔁
# Inverte a ordem dos elementos da lista
lista = [1, 2, 3]
lista.reverse()

# LEN 📏
# Retorna o número de elementos da lista
len(lista)

# SORT 📊
# Ordena a lista (modifica a original)
linguagens = ["python", "js", "c", "java", "csharp"]
linguagens.sort()  # Alfabética
linguagens.sort(reverse=True)  # Ordem reversa
linguagens.sort(key=lambda x: len(x))  # Por tamanho

# SORTED 🆕
# Cria uma nova lista ordenada (não altera a original)
linguagens = ["python", "js", "c", "java", "csharp"]
sorted(linguagens)
sorted(linguagens, key=len)
sorted(linguagens, key=len, reverse=True)

# POP ✂️
# Remove e retorna o item no índice (ou o último se vazio)
linguagens.pop()
linguagens.pop(0)

# REMOVE ❌
# Remove a primeira ocorrência do valor
linguagens.remove("js")
