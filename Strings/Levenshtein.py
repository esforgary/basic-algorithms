def levenshtein_distance(s1, s2):
    m, n = len(s1), len(s2)
    # Создаем матрицу с нулями для хранения расстояний
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    
    # Инициализируем первую строку и первый столбец матрицы
    for i in range(m + 1):
        dp[i][0] = i
    for j in range(n + 1):
        dp[0][j] = j
    
    # Заполняем матрицу по правилу динамического программирования
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if s1[i - 1] == s2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1]
            else:
                dp[i][j] = 1 + min(dp[i - 1][j - 1], dp[i - 1][j], dp[i][j - 1])
    
    # Возвращаем последнюю ячейку матрицы - минимальное расстояние
    return dp[m][n]


s1 = input("Введите исходную строку: ")
s2 = input("Введите строку, к котороц нужно прейти: ")
distance = levenshtein_distance(s1, s2)
print(f"Расстояние Левенштейна между строками '{s1}' и '{s2}' равно {distance}")