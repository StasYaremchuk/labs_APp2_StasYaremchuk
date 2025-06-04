def read_road_csv(filename):
    with open(filename, 'r') as f:
        lines = f.readlines()

    farms = [x.strip() for x in lines[0].split(',')]
    shops = [x.strip() for x in lines[1].split(',')]
    edges = []
    for line in lines[2:]:
        u, v, c = line.strip().split(',')
        edges.append((u.strip(), v.strip(), int(c.strip())))
    return farms, shops, edges


def build_graph(farms, shops, edges):
    graph = {}

    def add_edge(u, v, cap):
        if u not in graph:
            graph[u] = {}
        if v not in graph[u]:
            graph[u][v] = 0
        graph[u][v] += cap
        if v not in graph:
            graph[v] = {}
        if u not in graph[v]:
            graph[v][u] = 0

    for u, v, cap in edges:
        add_edge(u, v, cap)

    for farm in farms:
        add_edge('source', farm, 10 ** 10)

    for shop in shops:
        add_edge(shop, 'sink', 10 ** 10)

    return graph


def dfs(graph, u, sink, flow, visited):
    if u == sink:
        return flow
    visited.add(u)
    for v in graph[u]:
        if v not in visited and graph[u][v] > 0:
            curr_flow = min(flow, graph[u][v])
            temp_flow = dfs(graph, v, sink, curr_flow, visited)
            if temp_flow > 0:
                graph[u][v] -= temp_flow
                graph[v][u] += temp_flow
                return temp_flow
    return 0


def ford_fulkerson(filename):
    farms, shops, edges = read_road_csv(filename)
    graph = build_graph(farms, shops, edges)

    max_flow = 0
    while True:
        visited = set()
        flow = dfs(graph, 'source', 'sink', 10 ** 10, visited)
        if flow == 0:
            break
        max_flow += flow

    return max_flow


result = ford_fulkerson('roads.csv')
print("Максимальна кількість машин за день:", result)
