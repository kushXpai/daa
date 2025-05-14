from collections import deque

def bfs(graph, start_node, visited, directed):
    queue = deque([start_node])
    visited.add(start_node)
    bfs_order = []
    
    while queue:
        node = queue.popleft()
        bfs_order.append(node)
        
        if directed:
            neighbors = graph.get(node, [])
        else:
            neighbors = graph[node]
        
        for neighbor in neighbors:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)
    
    return bfs_order

def input_graph():
    graph = {}
    directed = input("Is the graph directed (yes/no)? ").strip().lower() == "yes"
    n = int(input("Enter the number of nodes: "))
    
    for i in range(n):
        node = input(f"Enter the name of node {i + 1}: ")
        graph[node] = []

    while True:
        edge_input = input(f"Enter an edge (node1 node2) or 'done' to finish: ").strip()
        if edge_input == "done":
            break
        node1, node2 = edge_input.split()
        graph[node1].append(node2)
        if not directed:
            graph[node2].append(node1)
    
    start_node = input("Enter the starting node for BFS: ").strip()
    return graph, start_node, directed

def bfs_for_all_components(graph, directed):
    visited = set()
    components = []
    
    for node in graph:
        if node not in visited:
            component = bfs(graph, node, visited, directed)
            components.append(component)
    
    return components

graph, start_node, directed = input_graph()

components = bfs_for_all_components(graph, directed)

for i, component in enumerate(components, 1):
    print(f"\nBFS Traversal for Component {i}:")
    print("BFS Traversal Order:", component)
    print("Total Nodes Visited:", len(component))