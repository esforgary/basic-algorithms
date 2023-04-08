import random

# Бесконечность для задания начальных расстояний
INF = float('inf')

def generate_graph(num_nodes, num_edges):
    # Создаем пустой граф с заданным количеством вершин
    graph = {str(i): {} for i in range(num_nodes)}

    # Добавляем случайные ребра в граф
    for _ in range(num_edges):
        u = random.randint(0, num_nodes-1)
        v = random.randint(0, num_nodes-1)
        while u == v or v in graph[str(u)]:
            u = random.randint(0, num_nodes-1)
            v = random.randint(0, num_nodes-1)
        weight = random.randint(1, 10)
        graph[str(u)][str(v)] = weight
        graph[str(v)][str(u)] = weight

    return graph


def dijkstra(graph, start):
    # Инициализация расстояний до всех вершин как бесконечность,
    # за исключением стартовой вершины, которая имеет расстояние 0
    distances = {node: INF for node in graph}
    distances[start] = 0

    # Создаем множество посещенных вершин
    visited = set()

    # Пока есть не посещенные вершины
    while len(visited) < len(graph):
        # Выбираем непосещенную вершину с минимальным расстоянием до нее из start
        node, node_distance = min((n, d) for (n, d) in distances.items() if n not in visited)

        # Добавляем эту вершину в список посещенных
        visited.add(node)

        # Проходимся по всем соседним вершинам
        for neighbor, weight in graph[node].items():
            # Обновляем расстояние до этой вершины, если мы можем пройти через node
            new_distance = distances[node] + weight
            if new_distance < distances[neighbor]:
                distances[neighbor] = new_distance

    return distances


# Создаем случайный граф с 5 вершинами и 8 ребрами
graph = generate_graph(5, 8)

# Выбираем случайную вершину в качестве стартовой
start = str(random.randint(0, 4))

# Ищем кратчайшие расстояния от стартовой вершины до всех остальных вершин в графе
distances = dijkstra(graph, start)

# Выводим результаты
print("Стартовая вершина:", start)
print("Граф:")
print(graph)
print("Кратчайшие расстояния:")
print(distances)
