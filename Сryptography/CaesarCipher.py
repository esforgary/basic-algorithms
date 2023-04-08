def caesar_cipher(message, key, mode):
    """
    Функция для шифрования или дешифрования сообщения с помощью шифра Цезаря.
    
    Аргументы:
    - message (str): исходное сообщение.
    - key (int): ключ шифрования (количество позиций, на которые будут сдвигаться буквы).
    - mode (str): режим работы функции ('encrypt' для шифрования и 'decrypt' для дешифрования).
    
    Возвращает:
    - result (str): зашифрованное или расшифрованное сообщение.
    """
    if mode == 'encrypt':
        key = key % 26 # если ключ больше 26, то буквы будут повторяться
    elif mode == 'decrypt':
        key = -key % 26 # для дешифрования необходимо сдвигать буквы в обратную сторону
    
    result = ""
    
    for char in message:
        if char.isalpha():
            char_code = ord(char.lower()) - 97 # код буквы от 0 до 25
            shifted_code = (char_code + key) % 26 # новый код буквы
            shifted_char = chr(shifted_code + 97) # новая буква
            result += shifted_char if char.islower() else shifted_char.upper() # сохраняем регистр
        else:
            result += char
    
    return result

message = "Hello, World!"
key = 4

encrypted_message = caesar_cipher(message, key, 'encrypt')
print("Зашифрованное сообщение:", encrypted_message)

decrypted_message = caesar_cipher(encrypted_message, key, 'decrypt')
print("Расшифрованное сообщение:", decrypted_message)
