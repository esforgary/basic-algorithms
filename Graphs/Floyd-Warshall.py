import random

def generate_random_graph(n, p):
    """
    Функция генерирует случайный граф на n вершинах с вероятностью p для каждой пары вершин
    Возвращает матрицу смежности графа в виде списка списков
    """
    graph = [[0 for j in range(n)] for i in range(n)]
    for i in range(n):
        for j in range(i+1, n):
            if random.random() < p:
                weight = random.randint(1, 10)
                graph[i][j] = weight
                graph[j][i] = weight
    return graph

def floyd_warshall(graph):
    """
    Функция реализует алгоритм Флойда-Уоршелла для нахождения всех кратчайших путей между парами вершин в графе
    Возвращает матрицу кратчайших расстояний между всеми парами вершин
    """
    n = len(graph)
    dist = [[float('inf') for j in range(n)] for i in range(n)]
    for i in range(n):
        for j in range(n):
            if i == j:
                dist[i][j] = 0
            elif graph[i][j] != 0:
                dist[i][j] = graph[i][j]

    for k in range(n):
        for i in range(n):
            for j in range(n):
                if dist[i][j] > dist[i][k] + dist[k][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]
    return dist


# пример использования
n = 5
p = 0.5
graph = generate_random_graph(n, p)
print("Матрица смежности случайного графа:")
for row in graph:
    print(row)
dist = floyd_warshall(graph)
print("Матрица кратчайших расстояний:")
for row in dist:
    print(row)