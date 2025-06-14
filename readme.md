# 🔐 Desafio de Cibersegurança – Ransomware Simulado

Este projeto é parte de um **desafio educacional** de cibersegurança, com o objetivo de simular o comportamento de um ransomware real — **criptografando e descriptografando arquivos** em uma estrutura de diretórios.

> ⚠️ **Aviso Legal:** Este projeto é para fins **educacionais** e de **aprendizado** apenas. Não utilize este código para fins maliciosos. A má utilização pode ser considerada crime, dependendo da legislação local.

---

## 📁 Estrutura do Projeto

cibersecurity-desafio-ransomware/
│
├── desafio/ # Pasta com arquivos e subpastas a serem criptografados
│ ├── exemplo.txt
│ └── subpasta/
│ └── exemplo2.txt
│
├── encrypter.py # Script para criptografar todos os arquivos
├── decrypt.py # Script para descriptografar todos os arquivos
│
├── encrypt.log # Log da criptografia (gerado automaticamente)
├── decrypt.log # Log da descriptografia (gerado automaticamente)
│
└── README.md # Este arquivo

---

## 🔐 Criptografia

- Utiliza o algoritmo **AES em modo CTR** com a biblioteca `pyaes`.
- Todos os arquivos da pasta `desafio/` (e subpastas) são criptografados e renomeados com a extensão `.ransomwaretroll`.
- O arquivo original é removido após a criptografia.
- Um log com os arquivos criptografados é salvo no `encrypt.log`.

### 📦 Instalação de dependências

Certifique-se de ter o Python instalado e depois rode no terminal:

pip install pyaes

## 🚀 Como Usar

### 1. Criptografar
python encrypter.py

### 2. Descriptografar
python decrypter.py

# 🧾 Logs
encrypt.log: Contém a lista de arquivos criptografados, com data e hora.

decrypt.log: Contém a lista de arquivos descriptografados, com data e hora.

#🛡️ Propósito Educacional
Este projeto ajuda a entender:

Como funciona a criptografia AES em modo CTR.
Como automatizar a criptografia de diretórios inteiros.
Boas práticas de logging e segurança.

