# Programação Orientada a Objetos (POO) em Python

A Programação Orientada a Objetos (POO) é um paradigma de programação que modela o software em termos de "objetos", que são instâncias de classes. Em Python, a POO é amplamente utilizada devido à sua sintaxe simples e recursos poderosos. A seguir, exploramos os principais pilares da POO em Python de forma detalhada.

---

## `self`

O `self` em Python é uma referência explícita ao objeto atual. Ele é o primeiro parâmetro de qualquer método de instância dentro de uma classe e permite acessar os atributos e métodos da própria instância.

```python
class Pessoa:
    def __init__(self, nome):
        self.nome = nome

    def falar(self):
        print(f"Olá, meu nome é {self.nome}")
```

Sem o `self`, não conseguimos distinguir entre variáveis locais e atributos da instância.

---

## Construtores (`__init__`) e Destrutores (`__del__`)

### Construtor `__init__`

É um método especial chamado automaticamente quando uma nova instância da classe é criada. Ele é usado para inicializar os atributos da instância.

```python
class Produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco
```

### Destrutor `__del__`

O método `__del__` é chamado quando o objeto está prestes a ser destruído (coletado pelo garbage collector). Seu uso é raro e deve ser feito com cautela.

```python
    def __del__(self):
        print(f"Objeto {self.nome} removido da memória")
```

> ⚠️ Em programas maiores, é preferível usar gerenciadores de contexto (`with`) para liberar recursos explicitamente.

---

## Herança

Permite que uma classe (subclasse) herde atributos e métodos de outra classe (superclasse).

### Herança Simples

```python
class Animal:
    def __init__(self, nome):
        self.nome = nome

    def emitir_som(self):
        print("Som genérico")

class Cachorro(Animal):
    def emitir_som(self):
        print("Au au")
```

### Herança Múltipla

Python permite que uma classe herde de múltiplas superclasses.

```python
class Aquatico:
    def nadar(self):
        print("Nadando...")

class Terrestre:
    def andar(self):
        print("Andando...")

class Sapo(Aquatico, Terrestre):
    pass
```

> Python usa o MRO (Method Resolution Order) para determinar a ordem de busca dos métodos na herança múltipla.

---

## Encapsulamento

Encapsulamento é o princípio de esconder os detalhes internos de implementação. Em Python, não há modificadores de acesso como `private` e `protected` explícitos, mas há convenções:

- `_atributo`: convenção para atributo "protegido"
- `__atributo`: nome "mangling" para dificultar acesso externo (simula "privado")

```python
class ContaBancaria:
    def __init__(self, saldo):
        self.__saldo = saldo  # privado

    def depositar(self, valor):
        self.__saldo += valor

    def ver_saldo(self):
        return self.__saldo
```

---

## Polimorfismo

Polimorfismo permite que diferentes classes tenham métodos com o mesmo nome, mas comportamentos distintos.

```python
class Ave:
    def emitir_som(self):
        print("Som de ave")

class Papagaio(Ave):
    def emitir_som(self):
        print("Loro quer biscoito")

class Corvo(Ave):
    def emitir_som(self):
        print("Croac croac")

for ave in [Papagaio(), Corvo()]:
    ave.emitir_som()
```

---

## Classes Abstratas

Uma classe abstrata serve como um modelo para outras classes. Não pode ser instanciada diretamente e define métodos que devem ser implementados nas subclasses. Em Python, usamos o módulo `abc` (Abstract Base Classes).

```python
from abc import ABC, abstractmethod

class FormaGeometrica(ABC):
    @abstractmethod
    def area(self):
        pass

class Quadrado(FormaGeometrica):
    def __init__(self, lado):
        self.lado = lado

    def area(self):
        return self.lado ** 2
```

Se a subclasse não implementar o método abstrato, ela também será considerada abstrata.

---

## Conclusão

A Programação Orientada a Objetos em Python fornece uma base sólida para criar códigos reutilizáveis, organizados e fáceis de manter. Com o domínio de `self`, construtores, herança, encapsulamento, polimorfismo e classes abstratas, você estará apto a modelar sistemas complexos de forma elegante e eficiente.
