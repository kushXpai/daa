def dfs(graph, node, visited, order):
    if node not in visited:
        visited.add(node)
        order.append(node)
        for neighbor in graph[node]:
            dfs(graph, neighbor, visited, order)

graph = {}
n = int(input("Enter number of nodes: "))
for _ in range(n):
    node = input("Enter node: ")
    neighbors = input(f"Enter neighbors of {node} separated by space: ").split()
    graph[node] = neighbors

start = input("Enter starting node: ")
visited = set()
order = []
dfs(graph, start, visited, order)
print("DFS Traversal Order:", order)
print("Total Nodes Visited:", len(visited))