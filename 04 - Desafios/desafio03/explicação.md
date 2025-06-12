# 💳 Projeto: Sistema Bancário com Programação Orientada a Objetos (POO)

## 🧾 Objetivo Geral

Desenvolver um sistema bancário simples utilizando os princípios da Programação Orientada a Objetos (POO), com foco em:

- Iniciar a modelagem de classes fundamentais para um sistema bancário.
- Adicionar classes para representar clientes e operações bancárias (depósito e saque).
- Substituir o uso de dicionários por objetos para representar entidades e suas interações.

---

## 🎯 Desafios Propostos

### ✅ Desafio Principal

Atualizar a implementação do sistema bancário para:

- Armazenar os dados de **clientes** e **contas bancárias** utilizando **objetos e classes**, em vez de estruturas simples como dicionários.
- Seguir um modelo de classes baseado em um diagrama UML proposto, utilizando herança, composição e encapsulamento.

### 💡 Desafio Extra

Após a modelagem das classes e métodos:

- Atualizar os **métodos que tratam as opções do menu** (depósito, saque, criação de conta, etc.), para funcionar com as novas classes modeladas.
- Garantir que as ações do sistema (como criar cliente, realizar depósito/saque, listar contas) estejam acopladas corretamente à lógica orientada a objetos.

---

## 🧩 Estrutura das Classes

A modelagem inclui as seguintes entidades principais:

### 👤 Cliente

- Classe base: `Cliente`
- Subclasse: `PessoaFisica`
- Atributos: nome, CPF, data de nascimento, endereço
- Métodos: associar contas, realizar transações

### 🏦 Conta

- Classe base: `Conta`
- Subclasse: `ContaCorrente`
- Atributos: número, saldo, agência, cliente, histórico
- Métodos: sacar, depositar

### 🔄 Transações

- Interface abstrata: `Transacao`
- Subclasses: `Saque` e `Deposito`
- Métodos: `registrar()` para aplicar a transação à conta

### 📜 Histórico

- Classe `Historico` para armazenar a lista de transações realizadas

---

## 🔧 Funcionalidades Implementadas

- [x] Criar cliente (com verificação por CPF)
- [x] Criar conta associada ao cliente
- [x] Realizar depósito com registro no histórico
- [x] Realizar saque com regras de limite e quantidade
- [x] Exibir extrato de uma conta
- [x] Listar todas as contas cadastradas

---

## 🖥️ Execução

O programa funciona em modo de terminal com menu interativo:

```text
=============== MENU ================
[d]    Depositar
[s]    Sacar
[e]    Extrato
[nc]   Nova conta
[lc]   Listar contas
[nu]   Novo usuário
[q]    Sair
=>
```
