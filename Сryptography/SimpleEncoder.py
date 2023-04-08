import string

def simple_substitution_encrypt(plaintext, key):
    """
    Шифрование сообщения методом простой подстановки.

    :param plaintext: исходное сообщение
    :param key: ключ для шифрования
    :return: зашифрованное сообщение
    """
    # Создаем словарь для подстановки
    substitution_dict = dict(zip(string.ascii_lowercase, key))

    # Зашифровываем сообщение
    ciphertext = ""
    for char in plaintext.lower():
        if char in substitution_dict:
            ciphertext += substitution_dict[char]
        else:
            ciphertext += char

    return ciphertext

def simple_substitution_decrypt(ciphertext, key):
    """
    Расшифрование сообщения, зашифрованного методом простой подстановки.

    :param ciphertext: зашифрованное сообщение
    :param key: ключ для расшифрования
    :return: расшифрованное сообщение
    """
    # Создаем словарь для обратной подстановки
    substitution_dict = dict(zip(key, string.ascii_lowercase))

    # Расшифровываем сообщение
    plaintext = ""
    for char in ciphertext.lower():
        if char in substitution_dict:
            plaintext += substitution_dict[char]
        else:
            plaintext += char

    return plaintext

# Пример использования
key = "qwertyuiopasdfghjklzxcvbnm"
plaintext = "hello world"
ciphertext = simple_substitution_encrypt(plaintext, key)
decrypted = simple_substitution_decrypt(ciphertext, key)

print("Исходное сообщение: ", plaintext)
print("Зашифрованное сообщение: ", ciphertext)
print("Расшифрованное сообщение: ", decrypted)
