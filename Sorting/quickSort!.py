from random import uniform, choice

def quickSort(nums):
   if len(nums) <= 1:
       return nums
   else:
       q = choice(nums)                                     # 1) Выбрать элемент из массива. Назовём его опорным.
  
   l_nums = [n for n in nums if n < q]                      # 2) Разбиение: перераспределение элементов в массиве таким образом, что элементы, 
   b_nums = [n for n in nums if n > q]                      #    меньшие опорного, помещаются перед ним, а большие или равные - после.
   e_nums = [q] * nums.count(q)

   return quickSort(l_nums) + e_nums + quickSort(b_nums)    # 3) Рекурсивно применить первые два шага к двум подмассивам слева и справа от опорного элемента. Рекурсия не применяется к массиву, в котором только один элемент или отсутствуют элементы.


def main():	
  try:
    array = [round(uniform(-10, 10), 2) for i in range(50)]

    print(array)
    res = quickSort(array)    
    print(f"\nОтсортированный масив: \n{res}")

  except:    
    print("\nНеверные данные !!!\n")

if __name__ == "__main__":
	main()