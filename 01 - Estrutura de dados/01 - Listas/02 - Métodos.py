# MÉTODOS DA CLASSE LIST EM PYTHON

# -------------------------------
# Append - Adiciona elementos no final da lista
lista = []  # Criando uma lista vazia

lista.append(1)                # Adiciona o número 1
lista.append("Python")         # Adiciona a string "Python"
lista.append([40, 30, 20])     # Adiciona outra lista como um único elemento

print(lista)  # Resultado: [1, 'Python', [40, 30, 20]]

# -------------------------------
# Copy - Cria uma cópia rasa da lista
lista2 = lista.copy()
print(lista2)  # Exibe a lista copiada
print(id(lista), id(lista2))  # Mostra que são listas diferentes (endereços de memória distintos)

# -------------------------------
# Count - Conta quantas vezes um elemento aparece na lista
cores = ["vermelho", "azul", "verde", "azul"]
print(cores.count("vermelho"), cores.count("azul"), cores.count("verde"))
# Saída: 1 2 1

# -------------------------------
# Extend - Adiciona os elementos de outra lista (descompacta e insere item por item)
cores.extend(["amarelo", "rosa"])
print(cores)  # Saída: ['vermelho', 'azul', 'verde', 'azul', 'amarelo', 'rosa']

# -------------------------------
# Index - Retorna o índice (posição) do primeiro elemento encontrado
print(cores.index("vermelho"), cores.index("azul"), cores.index("amarelo"))
# Saída: 0 1 4

# -------------------------------
# Clear - Remove todos os elementos da lista
lista.clear()
print(lista)  # Saída: []

# -------------------------------
# Reverse - Inverte a ordem dos elementos da lista
linguagens = ["python", "js", "c", "java", "csharp"]
linguagens.reverse()
print(linguagens)  # Saída: ['csharp', 'java', 'c', 'js', 'python']

# -------------------------------
# Len - Retorna o tamanho da lista ou do elemento
print(len(linguagens))      # Quantidade de elementos na lista → 5
print(len(linguagens[0]))   # Tamanho da string "csharp" → 6

# -------------------------------
# Sort - Ordena a lista (modifica a original)

# Ordem alfabética (crescente)
linguagens = ["python", "js", "c", "java", "csharp"]
linguagens.sort()
print(linguagens)  # Saída: ['c', 'csharp', 'java', 'js', 'python']

# Ordem alfabética reversa (decrescente)
linguagens = ["python", "js", "c", "java", "csharp"]
linguagens.sort(reverse=True)
print(linguagens)  # Saída: ['python', 'js', 'java', 'csharp', 'c']

# Ordem pelo tamanho das strings (menor para maior)
linguagens = ["python", "js", "c", "java", "csharp"]
linguagens.sort(key=lambda x: len(x))
print(linguagens)  # Saída: ['c', 'js', 'java', 'python', 'csharp']

# Ordem pelo tamanho das strings (maior para menor)
linguagens = ["python", "js", "c", "java", "csharp"]
linguagens.sort(key=lambda x: len(x), reverse=True)
print(linguagens)  # Saída: ['python', 'csharp', 'java', 'js', 'c']

# -------------------------------
# Sorted - Parecido com sort, mas não altera a lista original, apenas retorna uma nova lista ordenada
linguagens = ["python", "js", "c", "java", "csharp"]

# Ordena por tamanho (menor para maior)
print(sorted(linguagens, key=lambda x: len(x)))
# Saída: ['c', 'js', 'java', 'python', 'csharp']

# Ordena por tamanho (maior para menor)
print(sorted(linguagens, key=lambda x: len(x), reverse=True))
# Saída: ['python', 'csharp', 'java', 'js', 'c']

# -------------------------------
# Pop - Remove e retorna o último elemento (ou o índice especificado)
print(linguagens.pop(), linguagens.pop(), linguagens.pop(0))
# Remove e imprime: 'csharp', 'java', 'python'
print(linguagens)  # Restante: ['js', 'c']

# -------------------------------
# Remove - Remove o primeiro item com o valor especificado
linguagens.remove("c")
print(linguagens)  # Resultado: ['js']
