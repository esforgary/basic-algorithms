from random import randint

def countingSort(arr):
  size = len(arr)
  output = [0] * size
  count = [0] * size                      # инициализация массива подсчета

  for m in range(0, size):                # хранение количества каждого элемента
    count[arr[m]] += 1

  for m in range(1, size):                # сохранение совокупного количества
    count[m] += count[m - 1]

  m = size - 1
  while m >= 0:                           # помещение элементов в выходной массив после нахождения индекса каждого элемента исходного массива в массиве count
    output[count[arr[m]] - 1] = arr[m]
    count[arr[m]] -= 1
    m -= 1

  for m in range(0, size):
    arr[m] = output[m]


def main():	
  try:
    array = [randint(0, 49) for i in range(50)]

    print(array)
    countingSort(array)  
    print(f"\nОтсортированный масив: \n{array}")

  except ValueError:     
    print(ValueError)

if __name__ == "__main__":
	main()