from random import randint, choice

def quickSort(nums):
  if len(nums) <= 1:
    return nums
  else:
    q = choice(nums)

  l_nums = [n for n in nums if n < q]
  b_nums = [n for n in nums if n > q]
  e_nums = [q] * nums.count(q)

  return quickSort(l_nums) + e_nums + quickSort(b_nums) 
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 

def binaryAlgorithm(array, desired_value):
  first, last, mid, index = 0, len(array) - 1, 0, 0

  while (first <= last) and (array[index] != desired_value):
    mid = int((first + last) // 2)
    if array[mid] == desired_value:         # 1) Если mid — это тот элемент, который мы ищем (в лучшем случае), мы возвращаем его индекс.
      index = mid
    else:                                   # 2) Если нет, мы определяем, в какой половине массива мы будем искать desired_value дальше, основываясь на том,
      if desired_value < array[mid]:        #    меньше или больше значение desired_value значения mid, и отбрасываем вторую половину массива. 
        last = mid - 1                      
      else:                                 # 3) Затем мы рекурсивно или итеративно выполняем те же шаги, выбирая новое значение для mid, 
        first = mid + 1                     #    сравнивая его с desired_value и отбрасывая половину массива на каждой итерации алгоритма.
  
  if desired_value != array[index]:
    return '0'

  return index
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 

def main():	
  try:     
    array = [randint(-100, 100) for i in range(100)]
    array = quickSort(array)
    print(array)
    desired_value = int(input("Введите число, которое нужно найти: "))
    res = binaryAlgorithm(array, desired_value)

    if res == '0':
      print(f"\n{desired_value} не является элементом данного массива.\n") 
    else:
      print(f"Искомое значение ({desired_value}) находится под индексом {res}.\n")

  except:    
    print("\nНеверные данные !!!\n")    
if __name__ == "__main__":
	main()