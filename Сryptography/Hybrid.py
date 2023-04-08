from cryptography.fernet import Fernet
from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.primitives import serialization, hashes

# Генерация пары открытого и закрытого ключей RSA
private_key = rsa.generate_private_key(
    public_exponent=65537,  # Рекомендуемое значение
    key_size=2048  # Рекомендуемый размер ключа
)
public_key = private_key.public_key()

# Генерация ключа для симметричного шифрования
symmetric_key = Fernet.generate_key()

# Шифрование ключа симметричного шифрования с помощью открытого ключа RSA
encrypted_symmetric_key = public_key.encrypt(
    symmetric_key,
    padding.OAEP(
        mgf=padding.MGF1(algorithm=hashes.SHA256()),
        algorithm=hashes.SHA256(),
        label=None
    )
)

# Шифрование сообщения с помощью симметричного ключа
message = b"Hello, World!"
cipher_suite = Fernet(symmetric_key)
encrypted_message = cipher_suite.encrypt(message)
print("Encrypted message:", encrypted_message)

# Расшифровка ключа симметричного шифрования с помощью закрытого ключа RSA
decrypted_symmetric_key = private_key.decrypt(
    encrypted_symmetric_key,
    padding.OAEP(
        mgf=padding.MGF1(algorithm=hashes.SHA256()),
        algorithm=hashes.SHA256(),
        label=None
    )
)

# Расшифровка сообщения с помощью симметричного ключа
cipher_suite = Fernet(decrypted_symmetric_key)
decrypted_message = cipher_suite.decrypt(encrypted_message)
print("Decrypted message:", decrypted_message.decode())
