from collections import defaultdict
from random import randint

class Graph:                                            # Класс для представления графика
	def __init__(self, vertices):
		self.graph = defaultdict(list)                      # Cловарь, содержащий список смежности
		self.V = vertices
		self.matrix = [[0] * vertices for _ in range(vertices)]

	def addEdge(self, v1, v2):                              # Функция добавления ребра к графу
		self.graph[v1].append(v2)

		self.matrix[v1][v2] = 1

	def printEdges(self):                                 # Функция для печати ребер
		for v1, v2 in (self.graph).items(): 
			for v in v2:
				print(f"Из вершины ({v1})\t к вершинe ({v})")

	def topologicalSortUtil(self, v, visited, stack):     # Рекурсивная функция, используемая topologicalSort

		visited[v] = True                                   # Пометить текущий узел как посещенный.

		for i in self.graph[v]:                             # Повторить для всех вершин, смежных с этой вершиной
			if visited[i] == False:
				self.topologicalSortUtil(i, visited, stack)

		stack.insert(0, v)                                  # Помещаем текущую вершину в стек, в котором хранится результат

	def topologicalSort(self):                            # Функция топологической сортировки. Он использует рекурсивную topologicalSortUtil()

		visited = [False] * self.V                          # Отметить все вершины как не посещенные
		stack =[]

		for i in range(self.V):                             # Вызов рекурсивной вспомогательной функции для сохранения топологических
			if visited[i] == False:                     		  # Сортируем, начиная со всех вершин по очереди
				self.topologicalSortUtil(i, visited, stack)
				
		return stack

	def adjencyMatrix(self):                              # Матрица смежностей графа 
		for v1 in range(len(self.matrix)): 
			print()
			for v2 in range(len(self.matrix[v1])):
				print("{:4d}".format(self.matrix[v1][v2]), end = "")  


def main():	
  try:
    edgeCount = randint(5, 15)
    g = Graph(edgeCount)
    
    for rib in range(0, edgeCount):
      start = randint(0, edgeCount - 1)      
      end = randint(0, edgeCount - 1)
      g.addEdge(start, end)
       
    result = g.topologicalSort()
    print(f"\nКоличество вершин: {edgeCount}\n")
    g.printEdges()
    print(f"\nТопологическая сортировка графа:\n{result}\n")
    print("Матрица смежности:")
    g.adjencyMatrix()

  except ValueError:    
    print(ValueError)

if __name__ == "__main__":
	main()