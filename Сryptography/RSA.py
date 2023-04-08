from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.primitives import serialization, hashes

# Генерация пары открытого и закрытого ключей RSA
private_key = rsa.generate_private_key(
    public_exponent=65537,  # Рекомендуемое значение
    key_size=2048  # Рекомендуемый размер ключа
)
public_key = private_key.public_key()

# Шифрование сообщения
message = b"Hello, World!"
encrypted_message = public_key.encrypt(
    message,
    padding.OAEP(
        mgf=padding.MGF1(algorithm=hashes.SHA256()),
        algorithm=hashes.SHA256(),
        label=None
    )
)
print("Encrypted message:", encrypted_message.hex())

# Расшифровка сообщения
decrypted_message = private_key.decrypt(
    encrypted_message,
    padding.OAEP(
        mgf=padding.MGF1(algorithm=hashes.SHA256()),
        algorithm=hashes.SHA256(),
        label=None
    )
)
print("Decrypted message:", decrypted_message.decode())
