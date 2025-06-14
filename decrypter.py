import os
import pyaes
from datetime import datetime

base_dir = os.path.join(os.path.dirname(__file__), "desafio")
log_path = os.path.join(os.path.dirname(__file__), "decrypt.log")

key = b"testeransomwares"

def log(mensagem):
    with open(log_path, "a") as log_file:
        log_file.write(f"[{datetime.now()}] {mensagem}\n")

def descriptografar_arquivo(file_path):
    try:
        with open(file_path, "rb") as file:
            file_data = file.read()

        aes = pyaes.AESModeOfOperationCTR(key)
        decrypted_data = aes.decrypt(file_data)

        os.remove(file_path)

        new_file_path = file_path.replace(".ransomwaretroll", "")
        with open(new_file_path, "wb") as new_file:
            new_file.write(decrypted_data)

        log(f"Descriptografado: {file_path}")
        print(f"[OK] {new_file_path}")
    except Exception as e:
        log(f"Erro ao descriptografar {file_path}: {e}")
        print(f"[ERRO] {file_path}")

for root, dirs, files in os.walk(base_dir):
    for file_name in files:
        if file_name.endswith(".ransomwaretroll"):
            full_path = os.path.join(root, file_name)
            descriptografar_arquivo(full_path)
