# Estruturas de Dados em Python

Python oferece uma variedade de estruturas de dados nativas que permitem armazenar e organizar dados de maneira eficiente. As quatro estruturas de dados principais são listas, tuplas, conjuntos (sets) e dicionários. Cada uma possui características específicas que as tornam adequadas para diferentes situações.

## 1. Listas

As listas são estruturas de dados **ordenadas** e **mutáveis** que podem conter elementos de diferentes tipos.

### 1.1 Características

- **Ordenada**: mantém a ordem de inserção dos elementos
- **Mutável**: elementos podem ser modificados, adicionados ou removidos
- **Heterogênea**: pode conter diferentes tipos de dados
- **Indexada**: elementos podem ser acessados por índice (começando em 0)
- **Permite duplicatas**: elementos repetidos são permitidos

### 1.2 Criação

```python
# Lista vazia
lista_vazia = []
lista_vazia = list()

# Lista com valores iniciais
numeros = [1, 2, 3, 4, 5]
diversos = [42, "Python", True, 3.14]

# Lista por compreensão
quadrados = [x**2 for x in range(10)]

# Converter outros tipos para lista
lista_de_tupla = list((1, 2, 3))
lista_de_string = list("Python")  # ['P', 'y', 't', 'h', 'o', 'n']
```

### 1.3 Operações Comuns

```python
# Acesso por índice
primeiro = numeros[0]  # 1
ultimo = numeros[-1]   # 5

# Slicing (fatiamento)
subconjunto = numeros[1:3]  # [2, 3]
invertida = numeros[::-1]   # [5, 4, 3, 2, 1]

# Modificação
numeros[0] = 10  # [10, 2, 3, 4, 5]

# Adição de elementos
numeros.append(6)       # Adiciona ao final: [10, 2, 3, 4, 5, 6]
numeros.insert(1, 15)   # Insere na posição 1: [10, 15, 2, 3, 4, 5, 6]
numeros.extend([7, 8])  # Adiciona múltiplos valores: [10, 15, 2, 3, 4, 5, 6, 7, 8]

# Remoção
numeros.remove(3)       # Remove o valor 3: [10, 15, 2, 4, 5, 6, 7, 8]
valor = numeros.pop()   # Remove e retorna o último elemento: 8
valor = numeros.pop(0)  # Remove e retorna o elemento no índice 0: 10
del numeros[1]          # Remove o elemento no índice 1: [15, 4, 5, 6, 7]
numeros.clear()         # Remove todos os elementos: []

# Verificações
5 in numeros            # Verifica se 5 está na lista: True ou False
len(numeros)            # Retorna o número de elementos

# Ordenação
numeros.sort()          # Ordena in-place
numeros.sort(reverse=True)  # Ordena de forma decrescente
sorted(numeros)         # Retorna uma nova lista ordenada

# Reverter ordem
numeros.reverse()       # Inverte a ordem in-place
```

### 1.4 Métodos de Listas

| Método                             | Descrição                                                                             |
| ---------------------------------- | ------------------------------------------------------------------------------------- |
| `append(x)`                        | Adiciona um item ao final da lista                                                    |
| `extend(iterable)`                 | Adiciona todos os itens do iterável ao final da lista                                 |
| `insert(i, x)`                     | Insere um item na posição `i`                                                         |
| `remove(x)`                        | Remove o primeiro item com valor `x`                                                  |
| `pop([i])`                         | Remove e retorna o item na posição `i` (ou o último item se `i` não for especificado) |
| `clear()`                          | Remove todos os itens da lista                                                        |
| `index(x[, start[, end]])`         | Retorna o índice do primeiro item com valor `x`                                       |
| `count(x)`                         | Retorna o número de ocorrências de `x`                                                |
| `sort(*, key=None, reverse=False)` | Ordena a lista in-place                                                               |
| `reverse()`                        | Inverte os elementos da lista in-place                                                |
| `copy()`                           | Retorna uma cópia superficial da lista                                                |

### 1.5 Casos de Uso

- Armazenar sequências de elementos que podem mudar
- Manter uma ordem específica de itens
- Implementar pilhas e filas
- Armazenar registros em tabelas
- Operações frequentes de adição/remoção de elementos

## 2. Tuplas

As tuplas são estruturas de dados **ordenadas** e **imutáveis**, semelhantes às listas.

### 2.1 Características

- **Ordenada**: mantém a ordem de inserção dos elementos
- **Imutável**: uma vez criada, não pode ser modificada
- **Heterogênea**: pode conter diferentes tipos de dados
- **Indexada**: elementos podem ser acessados por índice
- **Permite duplicatas**: elementos repetidos são permitidos

### 2.2 Criação

```python
# Tupla vazia
tupla_vazia = ()
tupla_vazia = tuple()

# Tupla com valores
coordenadas = (10, 20)
pessoa = ("João", 30, "Engenheiro")

# Tupla com um único elemento (precisa da vírgula)
singleton = (42,)  # sem a vírgula seria apenas o inteiro 42

# Converter outros tipos para tupla
tupla_de_lista = tuple([1, 2, 3])
tupla_de_string = tuple("Python")  # ('P', 'y', 't', 'h', 'o', 'n')
```

### 2.3 Operações Comuns

```python
# Acesso por índice
x = coordenadas[0]  # 10
y = coordenadas[1]  # 20

# Slicing (similar às listas)
sub_tupla = pessoa[0:2]  # ("João", 30)

# Concatenação e multiplicação
coordenadas_3d = coordenadas + (30,)  # (10, 20, 30)
repetida = coordenadas * 3  # (10, 20, 10, 20, 10, 20)

# Verificações
30 in pessoa            # Verifica se 30 está na tupla: True
len(pessoa)             # Retorna o número de elementos: 3

# Métodos
pessoa.count(30)        # Conta ocorrências do valor: 1
pessoa.index("João")    # Retorna o índice do valor: 0

# Desempacotamento
nome, idade, profissao = pessoa  # Desempacota a tupla em variáveis

# Named tuples (tuplas nomeadas)
from collections import namedtuple
Ponto = namedtuple('Ponto', ['x', 'y'])
p = Ponto(11, 22)
print(p.x)  # 11
```

### 2.4 Métodos de Tuplas

Tuplas têm apenas dois métodos, devido à sua imutabilidade:

| Método                     | Descrição                                       |
| -------------------------- | ----------------------------------------------- |
| `count(x)`                 | Retorna o número de ocorrências de `x`          |
| `index(x[, start[, end]])` | Retorna o índice do primeiro item com valor `x` |

### 2.5 Casos de Uso

- Armazenar dados que não devem ser alterados
- Chaves de dicionários (listas não podem ser usadas como chaves)
- Retornar múltiplos valores de funções
- Dados heterogêneos que formam uma única entidade lógica
- Quando se deseja garantir que os dados não serão modificados acidentalmente

## 3. Conjuntos (Sets)

Conjuntos são coleções **não ordenadas** de elementos **únicos** e **imutáveis**.

### 3.1 Características

- **Não ordenado**: não mantém uma ordem específica
- **Mutável**: o conjunto em si pode ser modificado (adicionar/remover elementos)
- **Elementos imutáveis**: apenas objetos imutáveis (strings, números, tuplas) podem ser elementos
- **Não permite duplicatas**: elementos repetidos são ignorados automaticamente
- **Não indexado**: elementos não podem ser acessados por índice

### 3.2 Criação

```python
# Conjunto vazio
conjunto_vazio = set()  # Não pode usar {} vazio, pois isso cria um dicionário

# Conjunto com valores
numeros = {1, 2, 3, 4, 5}
frutas = {"maçã", "banana", "laranja"}

# Converter outros tipos para conjunto
conjunto_de_lista = set([1, 2, 2, 3, 3, 3])  # {1, 2, 3} (duplicatas removidas)
conjunto_de_string = set("mississippi")      # {'m', 'i', 's', 'p'} (caracteres únicos)

# Frozen set (conjunto imutável)
imutavel = frozenset([1, 2, 3])
```

### 3.3 Operações Comuns

```python
# Adição de elementos
numeros.add(6)              # Adiciona um elemento: {1, 2, 3, 4, 5, 6}
numeros.update([6, 7, 8])   # Adiciona múltiplos elementos: {1, 2, 3, 4, 5, 6, 7, 8}

# Remoção
numeros.remove(3)     # Remove o elemento 3 (gera erro se não existir)
numeros.discard(10)   # Remove o elemento 10 se existir (não gera erro)
valor = numeros.pop() # Remove e retorna um elemento arbitrário
numeros.clear()       # Remove todos os elementos

# Verificações
5 in numeros          # Verifica se 5 está no conjunto
len(numeros)          # Retorna o número de elementos

# Operações matemáticas de conjuntos
A = {1, 2, 3, 4}
B = {3, 4, 5, 6}

# União
C = A | B             # {1, 2, 3, 4, 5, 6}
C = A.union(B)        # Mesmo resultado

# Interseção
D = A & B             # {3, 4}
D = A.intersection(B) # Mesmo resultado

# Diferença
E = A - B             # {1, 2}
E = A.difference(B)   # Mesmo resultado

# Diferença simétrica
F = A ^ B              # {1, 2, 5, 6}
F = A.symmetric_difference(B)  # Mesmo resultado

# Subconjunto e superconjunto
A.issubset(B)         # False
A.issuperset(B)       # False
{1, 2}.issubset(A)    # True
```

### 3.4 Métodos de Conjuntos

| Método                            | Descrição                                            |
| --------------------------------- | ---------------------------------------------------- |
| `add(elem)`                       | Adiciona um elemento ao conjunto                     |
| `update(iterable)`                | Adiciona múltiplos elementos                         |
| `remove(elem)`                    | Remove um elemento (levanta KeyError se não existir) |
| `discard(elem)`                   | Remove um elemento se existir                        |
| `pop()`                           | Remove e retorna um elemento arbitrário              |
| `clear()`                         | Remove todos os elementos                            |
| `union(other_set)`                | Retorna a união de conjuntos                         |
| `intersection(other_set)`         | Retorna a interseção de conjuntos                    |
| `difference(other_set)`           | Retorna a diferença de conjuntos                     |
| `symmetric_difference(other_set)` | Retorna a diferença simétrica                        |
| `issubset(other_set)`             | Verifica se é subconjunto                            |
| `issuperset(other_set)`           | Verifica se é superconjunto                          |
| `isdisjoint(other_set)`           | Verifica se não há interseção                        |
| `copy()`                          | Retorna uma cópia do conjunto                        |

### 3.5 Casos de Uso

- Remover duplicatas de uma sequência
- Testes de pertinência rápidos (mais eficientes que listas)
- Operações matemáticas de conjuntos (união, interseção, etc.)
- Eliminação de dados redundantes
- Verificação de elementos únicos

## 4. Dicionários

Dicionários são coleções **não ordenadas** de pares **chave-valor**, onde cada chave é única.

### 4.1 Características

- **Não ordenado**: tradicionalmente não mantém uma ordem específica (a partir do Python 3.7, preserva a ordem de inserção)
- **Mutável**: elementos podem ser modificados, adicionados ou removidos
- **Indexado por chave**: valores são acessados pela chave, não por posição
- **Chaves únicas**: cada chave só pode aparecer uma vez no dicionário
- **Chaves imutáveis**: apenas objetos imutáveis (strings, números, tuplas) podem ser chaves

### 4.2 Criação

```python
# Dicionário vazio
dict_vazio = {}
dict_vazio = dict()

# Dicionário com valores iniciais
pessoa = {"nome": "João", "idade": 30, "profissao": "Engenheiro"}
coordenadas = {(0, 0): "Origem", (10, 20): "Ponto A"}

# Criação com dict()
config = dict(host="localhost", porta=8080, debug=True)

# Criação com pares de itens
items = [("a", 1), ("b", 2)]
d = dict(items)  # {'a': 1, 'b': 2}

# Dict comprehension
quadrados = {x: x**2 for x in range(6)}  # {0: 0, 1: 1, 2: 4, 3: 9, 4: 16, 5: 25}
```

### 4.3 Operações Comuns

```python
# Acesso a valores
nome = pessoa["nome"]        # "João"
idade = pessoa.get("idade")  # 30
# Diferença: get() não gera erro se a chave não existir, retorna None ou um valor padrão
endereco = pessoa.get("endereco", "Não informado")  # "Não informado"

# Modificação
pessoa["idade"] = 31  # Atualiza valor
pessoa["endereco"] = "Rua A"  # Adiciona novo par

# Verificações
"nome" in pessoa      # Verifica se a chave existe: True
len(pessoa)           # Retorna o número de pares: 4

# Remoção
del pessoa["profissao"]    # Remove o par pela chave
valor = pessoa.pop("idade")  # Remove e retorna o valor
ultimo_item = pessoa.popitem()  # Remove e retorna o último par inserido
pessoa.clear()             # Remove todos os pares

# Iteração
for chave in pessoa:               # Itera pelas chaves
    print(chave, pessoa[chave])

for chave, valor in pessoa.items():  # Itera pelos pares
    print(chave, valor)

for valor in pessoa.values():       # Itera pelos valores
    print(valor)

# Métodos dict
pessoa.update({"idade": 32, "cidade": "São Paulo"})  # Atualiza e adiciona múltiplos pares
pessoa_copia = pessoa.copy()  # Cria uma cópia superficial
```

### 4.4 Métodos de Dicionários

| Método                        | Descrição                                                       |
| ----------------------------- | --------------------------------------------------------------- |
| `get(key[, default])`         | Retorna o valor da chave ou default se não existir              |
| `items()`                     | Retorna uma visão de todos os pares (chave, valor)              |
| `keys()`                      | Retorna uma visão de todas as chaves                            |
| `values()`                    | Retorna uma visão de todos os valores                           |
| `update([other])`             | Atualiza o dicionário com os pares de outro dicionário/iterável |
| `pop(key[, default])`         | Remove e retorna o valor da chave (ou default)                  |
| `popitem()`                   | Remove e retorna um par (último inserido em Python 3.7+)        |
| `clear()`                     | Remove todos os elementos                                       |
| `setdefault(key[, default])`  | Retorna valor da chave, ou insere key:default e retorna default |
| `fromkeys(iterable[, value])` | Cria dicionário com chaves do iterável e valores iguais a value |
| `copy()`                      | Retorna uma cópia superficial do dicionário                     |

### 4.5 Casos de Uso

- Mapear chaves para valores
- Armazenar dados de configuração
- Contagem de frequências
- Cache de resultados
- Representar objetos com atributos
- Implementar grafos e árvores

## 5. Comparativo entre as Estruturas de Dados

| Característica         | Lista            | Tupla           | Conjunto         | Dicionário                   |
| ---------------------- | ---------------- | --------------- | ---------------- | ---------------------------- |
| Sintaxe                | `[1, 2, 3]`      | `(1, 2, 3)`     | `{1, 2, 3}`      | `{'a': 1, 'b': 2}`           |
| Ordenação              | Sim              | Sim             | Não              | Sim (a partir do Python 3.7) |
| Mutabilidade           | Sim              | Não             | Sim              | Sim                          |
| Elementos duplicados   | Sim              | Sim             | Não              | Não (chaves)                 |
| Indexação              | Por posição      | Por posição     | Não permitida    | Por chave                    |
| Uso típico             | Coleção ordenada | Dados imutáveis | Elementos únicos | Mapeamento chave-valor       |
| Complexidade de acesso | O(1)             | O(1)            | O(1)             | O(1)                         |
| Complexidade de busca  | O(n)             | O(n)            | O(1)             | O(1)                         |
| Memória utilizada      | Média            | Baixa           | Alta             | Alta                         |

## 6. Estruturas de Dados Especializadas

Além das estruturas básicas, Python oferece estruturas de dados especializadas no módulo `collections`:

### 6.1 deque

Fila de duas pontas que permite adição e remoção eficiente nas extremidades.

```python
from collections import deque

d = deque([1, 2, 3])
d.append(4)         # [1, 2, 3, 4]
d.appendleft(0)     # [0, 1, 2, 3, 4]
d.pop()             # 4 -> [0, 1, 2, 3]
d.popleft()         # 0 -> [1, 2, 3]
d.extend([4, 5])    # [1, 2, 3, 4, 5]
d.extendleft([0])   # [0, 1, 2, 3, 4, 5]
d.rotate(1)         # [5, 0, 1, 2, 3, 4]
```

### 6.2 Counter

Dicionário especializado para contagem de elementos.

```python
from collections import Counter

c = Counter("mississippi")  # {'i': 4, 's': 4, 'p': 2, 'm': 1}
c.most_common(2)           # [('i', 4), ('s', 4)]
c["s"] += 1                # {'i': 4, 's': 5, 'p': 2, 'm': 1}
c.update("missouri")       # Adiciona contagens de outra palavra
```

### 6.3 defaultdict

Dicionário com valor padrão para chaves inexistentes.

```python
from collections import defaultdict

# Cria dicionário que retorna 0 para chaves inexistentes
d = defaultdict(int)
d["a"] += 1  # {'a': 1}
print(d["b"])  # 0 (não levanta KeyError)

# Criando listas para cada chave
grupos = defaultdict(list)
for item in [("A", 1), ("B", 2), ("A", 3)]:
    grupos[item[0]].append(item[1])
# {'A': [1, 3], 'B': [2]}
```

### 6.4 OrderedDict

Dicionário que mantém a ordem de inserção (obsoleto a partir do Python 3.7, onde dicionários padrão já mantêm ordem).

```python
from collections import OrderedDict

d = OrderedDict([('a', 1), ('b', 2), ('c', 3)])
d['d'] = 4  # A ordem 'a', 'b', 'c', 'd' é preservada
d.move_to_end('b')  # Move 'b' para o final: 'a', 'c', 'd', 'b'
d.popitem(last=False)  # Remove o primeiro item ('a')
```

### 6.5 namedtuple

Tuplas com campos nomeados.

```python
from collections import namedtuple

Ponto = namedtuple('Ponto', ['x', 'y', 'z'])
p = Ponto(1, 2, 3)
print(p.x, p.y, p.z)  # 1 2 3
print(p[0], p[1], p[2])  # 1 2 3
x, y, z = p  # Desempacotamento
```

## 7. Dicas e Melhores Práticas

1. **Escolha a estrutura adequada para seu caso de uso**:

   - Precisa manter a ordem e modificar elementos? → Lista
   - Dados que não devem mudar? → Tupla
   - Elementos únicos sem ordem específica? → Conjunto
   - Precisa mapear chaves para valores? → Dicionário

2. **Cuidado com referências**:

   ```python
   lista1 = [1, 2, 3]
   lista2 = lista1  # Ambas variáveis referenciam a mesma lista!
   lista2.append(4) # Modifica lista1 também
   lista3 = lista1.copy()  # Cria uma cópia independente
   ```

3. **Use compreensões para código mais conciso**:

   ```python
   # Lista de quadrados dos números ímpares
   quadrados_impares = [x**2 for x in range(10) if x % 2 == 1]

   # Dicionário de número:quadrado
   quadrados_dict = {x: x**2 for x in range(5)}

   # Conjunto de letras únicas
   letras = {c for c in "mississippi"}
   ```

4. **Cuidado com mutabilidade em estruturas aninhadas**:

   ```python
   # Criando cópia superficial
   lista_orig = [1, [2, 3], 4]
   lista_copia = lista_orig.copy()  # ou list(lista_orig)

   # Modificação em elemento mutável afeta ambas
   lista_copia[1].append(5)  # lista_orig também muda: [1, [2, 3, 5], 4]

   # Para cópia profunda
   import copy
   lista_copia_profunda = copy.deepcopy(lista_orig)
   ```

5. **Use desempacotamento para atribuições múltiplas**:

   ```python
   # Tupla para múltiplas variáveis
   x, y, z = (1, 2, 3)

   # Troca de valores sem variável temporária
   a, b = b, a

   # Desempacotar com * para "resto" dos valores
   primeiro, *meio, ultimo = [1, 2, 3, 4, 5]  # primeiro=1, meio=[2,3,4], ultimo=5
   ```

6. **Verifique a existência de chaves em dicionários com segurança**:

   ```python
   # Evite isso (pode levantar KeyError):
   if dic["chave"] == valor:
       # ...

   # Melhor assim:
   if "chave" in dic and dic["chave"] == valor:
       # ...

   # Ou usando get:
   if dic.get("chave") == valor:
       # ...
   ```

7. **Use collections para casos específicos**:

   - `Counter` para contagens
   - `defaultdict` para valores padrão
   - `deque` para filas eficientes
   - `namedtuple` para tuplas com campos nomeados

8. **Operações de conjuntos são mais eficientes**:

   ```python
   # Para checar se um valor está numa coleção:
   if valor in set(lista):  # mais rápido para listas grandes
       # ...

   # Para encontrar elementos comuns:
   comuns = set(lista1) & set(lista2)  # interseção
   ```

9. **Não use dicionários para agrupar pequenos dados relacionados**:

   ```python
   # Evite:
   pessoa = {"nome": "João", "idade": 30}

   # Prefira:
   from collections import namedtuple
   Pessoa = namedtuple("Pessoa", ["nome", "idade"])
   pessoa = Pessoa("João", 30)
   ```

10. **Use sort() para ordenação in-place e sorted() para criar nova lista ordenada**:

    ```python
    # Modifica a lista original
    lista.sort()

    # Retorna nova lista ordenada sem modificar a original
    nova_lista = sorted(lista)
    ```
