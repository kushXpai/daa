import heapq

def dijkstra(graph, start):
    distances = {node: float('inf') for node in graph}
    distances[start] = 0
    pq = [(0, start)]
    while pq:
        current_distance, current_node = heapq.heappop(pq)
        if current_distance > distances[current_node]:
            continue
        for neighbor, weight in graph[current_node].items():
            distance = current_distance + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(pq, (distance, neighbor))
    return distances

graph = {}
n = int(input("Enter number of nodes: "))
for _ in range(n):
    node = input("Enter node: ")
    neighbors_count = int(input(f"Enter number of neighbors for {node}: "))
    graph[node] = {}
    for _ in range(neighbors_count):
        neighbor, weight = input(f"Enter neighbor and weight for {node} separated by space: ").split()
        graph[node][neighbor] = int(weight)

start = input("Enter starting node: ")
distances = dijkstra(graph, start)
print("Shortest distances from", start)
for node in distances:
    print(f"{node}: {distances[node]}")