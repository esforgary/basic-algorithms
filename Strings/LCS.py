def lcs(s1, s2):
    m, n = len(s1), len(s2)
    dp = [[0] * (n+1) for _ in range(m+1)]

    for i in range(1, m+1):
        for j in range(1, n+1):
            if s1[i-1] == s2[j-1]:
                dp[i][j] = dp[i-1][j-1] + 1
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])

    lcs_len = dp[m][n]
    lcs = [''] * lcs_len
    i, j = m, n

    while i > 0 and j > 0:
        if s1[i-1] == s2[j-1]:
            lcs[lcs_len-1] = s1[i-1]
            i -= 1
            j -= 1
            lcs_len -= 1
        elif dp[i-1][j] > dp[i][j-1]:
            i -= 1
        else:
            j -= 1

    return ''.join(lcs)


s1 = input("Введите первую строку: ")
s2 = input("Введите вторую строку: ")
result = lcs(s1, s2)
print(f"Расстояние Левенштейна между строками '{s1}' и '{s2}' равно {result}")