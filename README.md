# 📡 UDP_Redes - Análise Estatística via Sockets UDP

Projeto acadêmico que simula uma aplicação **cliente-servidor** utilizando o protocolo **UDP** em Python. A comunicação é realizada via sockets e permite a análise de dados numéricos contidos em arquivos `.txt`, com suporte à **concorrência** por meio de **multithreading**.

---

## 🎯 Objetivo

Desenvolver uma aplicação capaz de:
- Ler arquivos de até **1KB** contendo **números (um por linha)**;
- Enviar esse conteúdo para o servidor via **UDP**, juntamente com uma flag que indica a operação desejada;
- Processar o conteúdo do lado do servidor;
- Retornar os resultados ao cliente de forma precisa e formatada.

---

## ⚙️ Tecnologias Utilizadas

- Python 3.x
- `socket` (comunicação UDP)
- `threading` (concorrência com múltiplos clientes)
- Terminal / Prompt de Comando

---

## 📁 Estrutura do Projeto

```
UDP_Redes/
├── cliente.py              # Código do cliente UDP
├── servidor.py             # Código do servidor UDP
└── exemplo_arquivo.txt     # Arquivo de entrada com números (exemplo)
```

---

## 🚀 Como Executar o Projeto

### 1. Clone este repositório:

```bash
git clone https://github.com/CissaMachado/UDP_Redes.git
cd UDP_Redes
```

### 2. Inicie o servidor:

```bash
python servidor.py
```

### 3. Em outro terminal, execute o cliente:

```bash
python cliente.py
```

---

## 📄 Regras para o Arquivo de Entrada

- Deve conter **apenas números** (um por linha).
- Tamanho máximo: **1KB**.
- Exemplo válido:

```
5
12
3.5
8
```

---

## 🔢 Operações Disponíveis

As operações são definidas por **flags** digitadas pelo usuário no cliente:

| Flag | Operação                       |
|------|--------------------------------|
| 1    | Soma dos números               |
| 2    | Média dos números              |
| 3    | Maior e menor número           |
| 4    | Encerrar o servidor (teste)    |

---

## 🛡️ Tratamento de Erros

- ⚠️ Arquivo vazio ou com conteúdo inválido
- ⚠️ Arquivo acima de 1KB
- ⚠️ Flag inexistente ou inválida

Todas as situações acima são **tratadas com mensagens apropriadas** ao cliente.

---

## 👩‍💻 Desenvolvedora

[Cecília Machado](https://github.com/CissaMachado)  
Graduanda em Sistemas para Internet – IFRS
💡 Projeto realizado como parte da disciplina de Redes de Computadores (2025)

---

## 📆 Data da Apresentação

**05/06/2025**

---

## 📝 Licença

Este projeto é de uso acadêmico. Sinta-se livre para estudar, adaptar e aprender com ele. 🌱
