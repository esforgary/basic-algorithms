from random import uniform

def radix_sort(arr):
    # Находим максимальный элемент в массиве
    max_element = max(arr)

    # Находим количество цифр в максимальном элементе
    digits = len(str(abs(max_element)))

    # Применяем сортировку подсчетом для каждой цифры
    for i in range(digits):
        # Создаем список подсчета для каждой цифры
        count = [0] * 10

        # Заполняем список подсчета значениями из массива
        for j in range(len(arr)):
            index = (arr[j] // 10 ** i) % 10
            count[index] += 1

        # Вычисляем сумму значений в списке подсчета
        for j in range(1, 10):
            count[j] += count[j - 1]

        # Создаем временный список для сохранения отсортированных значений
        temp = [0] * len(arr)

        # Заполняем временный список отсортированными значениями
        for j in range(len(arr) - 1, -1, -1):
            index = (arr[j] // 10 ** i) % 10
            temp[count[index] - 1] = arr[j]
            count[index] -= 1

        # Копируем отсортированные значения из временного списка в исходный массив
        for j in range(len(arr)):
            arr[j] = temp[j]

    # Разделяем список на два: отрицательные и положительные элементы
    neg_lst = [x for x in arr if x < 0]
    pos_lst = [x for x in arr if x >= 0]

    # Склеиваем списки и возвращаем отсортированный список
    return neg_lst + pos_lst


arr = [round(uniform(-101, 100)) for i in range(10)]
print(radix_sort(arr))
