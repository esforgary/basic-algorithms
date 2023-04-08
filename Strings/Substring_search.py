def find_substring(string, substring):
    index = 0
    while index <= len(string) - len(substring):
        if string[index:index+len(substring)] == substring:
            return index
        index += 1
    return -1

string = input("Предложение: ")
substring = input("Поиск: ц")
index = find_substring(string, substring)
if index >= 0:
    print(f"Подстрока '{substring}' найдена в строке '{string}' на позиции {index}.")
else:
    print(f"Подстрока '{substring}' не найдена в строке '{string}'.")
