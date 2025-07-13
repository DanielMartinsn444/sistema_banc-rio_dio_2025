# 🏦 Sistema Bancário em Python

Este projeto é um sistema bancário simples feito em Python como parte de um desafio de bootcamp.  
O sistema roda no terminal e oferece funcionalidades básicas de um banco, como:

- Depósitos
- Saques
- Extrato bancário
- Limite de saque diário
- Controle de saldo
- Cadastro de usuários
- Em breve...

---

## 💡 Funcionalidades

✅ *Depósito*  
- Permite inserir um valor positivo na conta  
- Atualiza o saldo e registra no extrato

✅ *Saque*  
- Permite realizar saques com regras:
  - Limite máximo de R$500 por saque
  - Máximo de 3 saques por dia
  - Valor deve ser positivo e não pode ultrapassar o saldo
- Atualiza o saldo e registra no extrato

✅ *Extrato*  
- Exibe todas as movimentações realizadas (depósitos e saques)  
- Mostra o saldo atual

✅ *Criar Usuário*  
- Crie um usuário (Feature Recente)
- Mostra quem está cadastrado.
- Possibilita armazenamento de informações
   
✅ Nova Feature em breve...

✅ *Saída*  
- Encerra o programa de forma limpa

---

## 🧪 Como usar

1. Clone o repositório ou copie o código para um arquivo .py
2. Execute no terminal com Python 3:
   ```bash
   python banco.py
