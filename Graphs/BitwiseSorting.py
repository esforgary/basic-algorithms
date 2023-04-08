def topological_sort(graph):
    # Создаем словарь зависимостей для каждой вершины
    dependencies = {vertex: set() for vertex in graph}
    for vertex in graph:
        for dependent_vertex in graph[vertex]:
            dependencies[dependent_vertex].add(vertex)

    # Создаем список вершин без предшественников
    vertices_without_dependencies = [vertex for vertex in graph if not dependencies[vertex]]

    # Создаем отсортированный список вершин
    sorted_vertices = []
    while vertices_without_dependencies:
        # Выбираем вершину без предшественников
        vertex = vertices_without_dependencies.pop()
        sorted_vertices.append(vertex)

        # Удаляем вершину из зависимостей других вершин
        for dependent_vertex in graph[vertex]:
            dependencies[dependent_vertex].remove(vertex)
            # Если все зависимости другой вершины удовлетворены, добавляем ее в список вершин без предшественников
            if not dependencies[dependent_vertex]:
                vertices_without_dependencies.append(dependent_vertex)

    return sorted_vertices


graph = {
    'A': ['B', 'C'],
    'C': ['D'],
    'D': [],
    'B': ['C', 'D']
}

r = topological_sort(graph)
print(r)