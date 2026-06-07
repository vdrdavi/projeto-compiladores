# Gerenciador de Tabela de Símbolos

Este projeto implementa um Gerenciador de Tabela de Símbolos, simulando o comportamento de escopos aninhados em compiladores através do uso de uma Pilha de Hash Tables (dicionários em Python).

## Pré-requisitos
- Python 3.x instalado no sistema.

## Como executar
Siga os comandos exatos de terminal abaixo para executar o projeto:

1. Clone o repositório:
`git clone https://github.com/vdrdavi/projeto-compiladores `

2. Acesse a pasta raiz do projeto:
`cd projeto-compiladores`

3. Execute o script principal:
`python tabela_simbolos.py`

## Funcionalidades Demonstradas na Execução
Ao rodar o comando acima, o sistema executará automaticamente uma série de testes que imprimem no terminal:
- Declaração e busca em escopo global.
- Entrada em novo escopo (local).
- Sombreamento de variáveis (Shadowing) e herança de escopos superiores.
- Bloqueio de re-declaração de mesma variável no mesmo escopo.
- Saída de escopo e destruição de variáveis locais.
