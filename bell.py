def bellman_ford(graph, vertices, edges, start):
    distance = {v: float('inf') for v in vertices}
    distance[start] = 0
    for _ in range(len(vertices) - 1):
        for u, v, w in edges:
            if distance[u] != float('inf') and distance[u] + w < distance[v]:
                distance[v] = distance[u] + w
    for u, v, w in edges:
        if distance[u] != float('inf') and distance[u] + w < distance[v]:
            return None
    return distance

vertices = []
edges = []
n = int(input("Enter number of vertices: "))
for _ in range(n):
    vertices.append(input("Enter vertex: "))

e = int(input("Enter number of edges: "))
for _ in range(e):
    u, v, w = input("Enter edge (u v w): ").split()
    edges.append((u, v, int(w)))

start = input("Enter starting vertex: ")
distances = bellman_ford({}, vertices, edges, start)
if distances is None:
    print("Graph contains a negative weight cycle")
else:
    print("Shortest distances from", start)
    for vertex in distances:
        print(f"{vertex}: {distances[vertex]}")