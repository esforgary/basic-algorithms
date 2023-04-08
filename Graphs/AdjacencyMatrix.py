def adjacency_matrix(graph):
    # Создаем список вершин графа
    vertices = list(graph.keys())
    # Создаем матрицу смежности и заполняем ее нулями
    matrix = [[0 for _ in range(len(vertices))] for _ in range(len(vertices))]
    # Заполняем матрицу смежности значениями из словаря
    for i in range(len(vertices)):
        for neighbor in graph[vertices[i]]:
            j = vertices.index(neighbor)
            matrix[i][j] = 1
    return matrix

# Пример использования
graph = {
    'A': ['B', 'C'],
    'B': ['C', 'D'],
    'C': ['D'],
    'D': []
}
matrix = adjacency_matrix(graph)
print(matrix)
