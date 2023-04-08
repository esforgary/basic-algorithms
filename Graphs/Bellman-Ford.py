import random

# Бесконечность для задания начальных расстояний
INF = float('inf')

def generate_random_graph(num_nodes, num_edges):
    # Создаем пустой граф с заданным количеством вершин
    graph = {str(i): {} for i in range(num_nodes)}

    # Добавляем случайные ребра в граф
    for _ in range(num_edges):
        u = random.randint(0, num_nodes-1)
        v = random.randint(0, num_nodes-1)
        while u == v or v in graph[str(u)]:
            u = random.randint(0, num_nodes-1)
            v = random.randint(0, num_nodes-1)
        weight = random.randint(-10, 10)
        graph[str(u)][str(v)] = weight

    return graph

def bellman_ford(graph, start):
    # Инициализация расстояний до всех вершин как бесконечность,
    # за исключением стартовой вершины, которая имеет расстояние 0
    distances = {node: INF for node in graph}
    distances[start] = 0

    # Проходимся по всем ребрам графа
    for _ in range(len(graph) - 1):
        for u in graph:
            for v, weight in graph[u].items():
                # Обновляем расстояние до вершины v, если мы можем пройти через u
                if distances[u] + weight < distances[v]:
                    distances[v] = distances[u] + weight

    # Проверяем наличие отрицательных циклов в графе
    negative_cycle = False
    for u in graph:
        for v, weight in graph[u].items():
            if distances[u] + weight < distances[v]:
                negative_cycle = True
                break

    if negative_cycle:
        return None, "Отрицательный цикл обнаружен!"

    return distances, None


# Задаем количество вершин и ребер в графе
num_nodes = 5
num_edges = 8

# Создаем случайный граф с помощью алгоритма Эрдеша-Реньи
graph = generate_random_graph(num_nodes, num_edges)

# Выбираем случайную вершину в качестве стартовой
start = str(random.randint(0, num_nodes-1))

# Ищем кратчайшие расстояния от стартовой вершины до всех остальных вершин в графе
distances = bellman_ford(graph, start)

# Выводим результаты
print("Стартовая вершина:", start)
print("Граф:")
print(graph)
print("Кратчайшие расстояния:")
print(distances)