import heapq

def dijkstra(graph, start):
    pq = [(0, start)]
    distances = {node: float('inf') for node in graph}
    distances[start] = 0
    
    while pq:
        current_distance, current_node = heapq.heappop(pq)
        
        if current_distance > distances[current_node]:
            continue
        
        for neighbor, weight in graph[current_node]:
            distance = current_distance + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(pq, (distance, neighbor))
    
    return distances

def main():
    graph = {}
    num_vertices = int(input("Enter number of vertices: "))
    num_edges = int(input("Enter number of edges: "))
    
    print("Enter edges in the format: source destination weight")
    for _ in range(num_edges):
        src, dest, weight = input().split()
        weight = int(weight)
        if src not in graph:
            graph[src] = []
        if dest not in graph:
            graph[dest] = []
        graph[src].append((dest, weight))
        graph[dest].append((src, weight))
    
    start_node = input("Enter the start node: ")
    shortest_paths = dijkstra(graph, start_node)
    
    print("Shortest distances from node", start_node)
    for node, distance in shortest_paths.items():
        print(f"Node {node}: {distance}")

if __name__ == "__main__":
    main()