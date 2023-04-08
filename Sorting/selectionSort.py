from random import uniform

def selectionSort(array):
  for i in range(len(array) - 1):
    _min = array[i]                         # 1) Найти наименьшее значение в списке.
    _min_index = i                          # 2) Записать его в начало списка, а первый элемент - на место, где раньше стоял наименьший.
    for j in range(i + 1, len(array)):
      if _min > array[j]:                   # 3) Снова найти наименьший элемент в списке. При этом в поиске не участвует первый элемент.
        _min = array[j]                     # 4) Второй минимум поместить на второе место списка. Второй элемент 
        _min_index = j                      #    при этом перемещается на освободившееся место.
    if _min_index != i:
      temp = array[i]
      array[i] = array[_min_index]
      array[_min_index] = temp              # 5) Продолжать выполнять поиcк и обмен, пока не будет достигнут конец списка.
  

def main():	
  try:
    array = [round(uniform(-100, 100), 2) for i in range(100)]

    print(array)
    selectionSort(array)    
    print(f"\nОтсортированный масив: \n{array}")

  except:    
    print("\nНеверные данные !!!\n")

if __name__ == "__main__":
	main()