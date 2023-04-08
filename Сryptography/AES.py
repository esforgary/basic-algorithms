from cryptography.fernet import Fernet

# Генерируем секретный ключ
key = Fernet.generate_key()

# Создаем объект класса Fernet с использованием секретного ключа
fernet = Fernet(key)

# Зашифровываем и расшифровываем сообщение
message = b"Hello, world!"
encrypted_message = fernet.encrypt(message)
decrypted_message = fernet.decrypt(encrypted_message)

print("Исходное сообщение:", message)
print("Зашифрованное сообщение:", encrypted_message)
print("Расшифрованное сообщение:", decrypted_message)


       