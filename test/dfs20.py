


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
    
    start_node = input("Enter the starting node for DFS: ").strip()
    return graph, start_node, directed

def dfs_for_all_components(graph, directed):
    visited = set()
    components = []
    
    for node in graph:
        if node not in visited:
            component = dfs(graph, node, visited, directed)
            components.append(component)
    
    return components

graph, start_node, directed = input_graph()

components = dfs_for_all_components(graph, directed)

for i, component in enumerate(components, 1):
    print(f"\nDFS Traversal for Component {i}:")
    print("DFS Traversal Order:", component)
    print("Total Nodes Visited:", len(component))