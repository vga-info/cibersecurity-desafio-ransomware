# 🔐 Desafio de Cibersegurança – Ransomware Simulado

Este projeto é parte de um **desafio educacional** de cibersegurança, com o objetivo de simular o comportamento de um ransomware real — **criptografando e descriptografando arquivos** em uma estrutura de diretórios.

> ⚠️ **Aviso Legal:** Este projeto é para fins **educacionais** e de **aprendizado** apenas. Não utilize este código para fins maliciosos. A má utilização pode ser considerada crime, dependendo da legislação local. 

---

## 🔐 Criptografia (encrypter.py)

- Utiliza o algoritmo **AES em modo CTR** com a biblioteca `pyaes`.
- Todos os arquivos da pasta `desafio/` (e subpastas) são criptografados e renomeados com a extensão `.ransomwaretroll`.
- O arquivo original é removido após a criptografia.
- Um log com os arquivos criptografados é salvo no `encrypt.log`.

## 🔐 Descriptografia (decrypter.py)
- O processo inverso da criptografia gerada pelo encrypter.py.
- Um log com os arquivos descriptografados é salvo no `decrypt.log`.


## 🚀 Como Usar

### 📦 Instalação de dependências
Certifique-se de ter o Python instalado e depois rode no terminal:

pip install pyaes

### 1. Criptografar
python encrypter.py

### 2. Descriptografar
python decrypter.py

# 🧾 Logs
encrypt.log: Contém a lista de arquivos criptografados, com data e hora.

decrypt.log: Contém a lista de arquivos descriptografados, com data e hora.

# 🛡️ Propósito Educacional
Este projeto ajuda a entender:

Como funciona a criptografia AES em modo CTR.
Como automatizar a criptografia de diretórios inteiros.
Boas práticas de logging e segurança.

*Desafio "implementar um Ransomware para criptografar arquivos utilizando a linguagem Python" proposto pelo instrutor Cassiano Peres no curso de Cybersegurança da DIO (dio.me)*
