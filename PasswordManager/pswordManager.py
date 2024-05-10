from cryptography.fernet import Fernet
import random
import string


#Armazenamento de senhas
password_list = []


#geração de senhas fortes
key = Fernet.generate_key()
password_list = password_list.append(key)
f = Fernet(key)
# token = f.encrypt(b"Secret message")
print(key)

#Segurança das senhas
cryptoKey = key.encrypt(b"****************")

#verificação de senhas
