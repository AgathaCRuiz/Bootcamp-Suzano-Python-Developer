# MÉTODOS E OPERAÇÕES COM CONJUNTOS (SET) EM PYTHON

# -------------------------------
# Union - Une dois conjuntos (sem duplicar elementos)
conjunto_a = {1, 2}
conjunto_b = {3, 4}

conjunto_c = conjunto_a.union(conjunto_b)
print(conjunto_c)  # Saída: {1, 2, 3, 4}

# -------------------------------
# Intersection - Retorna os elementos comuns entre os conjuntos
conjunto_a = {1, 2, 3}
conjunto_b = {2, 3, 4}

conjunto_c = conjunto_a.intersection(conjunto_b)
print(conjunto_c)  # Saída: {2, 3}

# -------------------------------
# Difference - Elementos que estão em um conjunto, mas não no outro
conjunto_a = {1, 2, 3}
conjunto_b = {2, 3, 4}

conjunto_c = conjunto_a.difference(conjunto_b)
print(conjunto_c)  # Saída: {1}

conjunto_c = conjunto_b.difference(conjunto_a)
print(conjunto_c)  # Saída: {4}

# -------------------------------
# Symmetric Difference - Elementos que estão em um ou outro, mas não em ambos
conjunto_a = {1, 2, 3}
conjunto_b = {2, 3, 4}

conjunto_c = conjunto_a.symmetric_difference(conjunto_b)
print(conjunto_c)  # Saída: {1, 4}

# -------------------------------
# issubset - Verifica se um conjunto é subconjunto de outro
conjunto_a = {1, 2, 3}
conjunto_b = {4, 1, 2, 5, 6, 3}

print(conjunto_a.issubset(conjunto_b))  # True → A está contido em B
print(conjunto_b.issubset(conjunto_a))  # False

# -------------------------------
# issuperset - Verifica se um conjunto é superconjunto de outro
print(conjunto_a.issuperset(conjunto_b))  # False
print(conjunto_b.issuperset(conjunto_a))  # True → B contém todos os elementos de A

# -------------------------------
# isdisjoint - Verifica se dois conjuntos são disjuntos (sem elementos em comum)
conjunto_a = {1, 2, 3, 4, 5}
conjunto_b = {6, 7, 8, 9}
conjunto_c = {1, 0}

print(conjunto_a.isdisjoint(conjunto_b))  # True → Nenhum elemento em comum
print(conjunto_a.isdisjoint(conjunto_c))  # False → O número 1 está em ambos

# -------------------------------
# Add - Adiciona um novo elemento ao conjunto
sorteio = {1, 23, 22}
sorteio.add(25)
print(sorteio)  # Saída: {1, 22, 23, 25}

# -------------------------------
# Copy - Cria uma cópia rasa do conjunto
copia_sorteio = sorteio.copy()
print(copia_sorteio)  # Saída: {1, 22, 23, 25}

# -------------------------------
# Clear - Remove todos os elementos do conjunto
sorteio.clear()
print(sorteio)  # Saída: set()

# -------------------------------
# Discard - Remove um elemento, se existir (não gera erro se não existir)
sorteio = {1, 22, 23}
sorteio.discard(1)
print(sorteio)  # Saída: {22, 23}

# -------------------------------
# Pop - Remove e retorna um elemento aleatório do conjunto
elemento = sorteio.pop()
print(elemento)     # Exibe o elemento removido
print(sorteio)      # Conjunto após a remoção

# -------------------------------
# Remove - Remove um elemento específico (gera erro se não existir)
sorteio = {22, 25}
sorteio.remove(22)
print(sorteio)  # Saída: {25}

# -------------------------------
# Len - Retorna a quantidade de elementos do conjunto
print(len(sorteio))  # Saída: 1
