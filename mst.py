def prims_algorithm(graph, V):
    selected = [False] * V
    edge_count = 0
    selected[0] = True
    mst_cost = 0

    print("\nEdge added to MST and their weights:")
    print("From  To   Weight")

    while edge_count < V - 1:
        minimum = float('inf')
        x = 0
        y = 0

        for i in range(V):
            if selected[i]:
                for j in range(V):
                    if not selected[j] and graph[i][j]:
                        if minimum > graph[i][j]:
                            minimum = graph[i][j]
                            x = i
                            y = j

        print(f"  {x}   - {y}     {graph[x][y]}")
        mst_cost += graph[x][y]
        selected[y] = True
        edge_count += 1

    print(f"\nTotal cost of MST: {mst_cost}")

V = int(input("Enter the number of vertices: "))

print("Enter the adjacency matrix (use 0 for no edge):")
graph = []

for i in range(V):
    row = list(map(int, input(f"Row {i}: ").split()))
    graph.append(row)

prims_algorithm(graph, V)