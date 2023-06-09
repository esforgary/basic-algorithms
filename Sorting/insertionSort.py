from random import uniform

def insertionSort(array):
  for i in range(1, len(array)):          # так как мы хотим поменять местами элемент с предыдущим, мы начинаем с 1
    temp = array[i]                       # temp будет использоваться для сравнения с предыдущими элементами и отправлено на место, которому оно принадлежит
    j = i - 1                             # инициализируем предидущий элемент
    while (j >= 0 and temp < array[j]):   # j >= 0 потому что нет смысла идти до k[0], так как слева от него нет свободного места, для temp
      array[j + 1] = array[j]             # переместите больший элемент на 1 шаг влево, чтобы освободить место для временного
      j = j - 1                           # возьмем k[j] налево до того места, где слева от него меньше/нет значения.
    array[j + 1] = temp   

def main():	
  try:
    array = [round(uniform(-100, 100), 2) for i in range(100)]

    print(array)
    insertionSort(array)    
    print(f"\nОтсортированный масив: \n{array}")

  except:    
    print("\nНеверные данные !!!\n")

if __name__ == "__main__":
	main()

# 1) Перебираются элементы в неотсортированной части массива.

# 2) Каждый элемент вставляется в отсортированную часть массива на то место, где он должен находиться.