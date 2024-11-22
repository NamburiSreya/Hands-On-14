class Edge:
    def __init__(self, source, destination, cost):
        self.source = source
        self.destination = destination
        self.cost = cost

class Vertex:
    def __init__(self, label):
        self.label = label
        self.cost = float('inf')
        self.previous = None

def relax(u, v, weight):
    if v.cost > u.cost + weight:
        v.cost = u.cost + weight
        v.previous = u

def init_single_source(graph, start):
    for vertex in graph.vertices:
        vertex.cost = float('inf')
        vertex.previous = None
    start.cost = 0

def find_min_cost_vertex(unvisited):
    min_vertex = unvisited[0]
    for vertex in unvisited:
        if vertex.cost < min_vertex.cost:
            min_vertex = vertex
    unvisited.remove(min_vertex)
    return min_vertex

def dijkstra(graph, start):
    init_single_source(graph, start)
    visited = []
    unvisited = graph.vertices[:]
    while unvisited:
        u = find_min_cost_vertex(unvisited)
        visited.append(u)
        for v in graph.adjacency[u]:
            relax(u, v, graph.costs[(u, v)])
    return visited

def reconstruct_path(vertex):
    path = []
    while vertex:
        path.append(vertex.label)
        vertex = vertex.previous
    path.reverse()
    return path

class Graph:
    def __init__(self, vertices):
        self.vertices = vertices
        self.adjacency = {}
        self.costs = {}
        for vertex in vertices:
            self.adjacency[vertex] = []

    def add_edge(self, source, destination, cost):
        if source not in self.adjacency:
            self.adjacency[source] = [destination]
        else:
            self.adjacency[source].append(destination)
        self.costs[(source, destination)] = cost

    def __str__(self):
        result = "\n--- Adjacent Vertices ---\n"
        for vertex in self.adjacency:
            result += f"{vertex.label}: "
            result += " ".join(str(v.label) for v in self.adjacency[vertex])
            result += "\n"
        return result + "--- End of Adjacent Vertices ---\n"

if __name__ == "__main__":
    # Example from figure 24.6 of Chapter 24 of 2009 Introduction to Algorithms by Cormen et al.
    # s: 0, t: 1, x: 2, y: 3, z: 4

    vertices = [Vertex(i) for i in range(5)]

    edges = [Edge(vertices[0], vertices[1], 10),
             Edge(vertices[0], vertices[3], 5),
             Edge(vertices[1], vertices[2], 1),
             Edge(vertices[1], vertices[3], 2),
             Edge(vertices[2], vertices[4], 4),
             Edge(vertices[3], vertices[1], 3),
             Edge(vertices[3], vertices[2], 9),
             Edge(vertices[3], vertices[4], 2),
             Edge(vertices[4], vertices[0], 7),
             Edge(vertices[4], vertices[2], 6)]

    graph = Graph(vertices)
    for edge in edges:
        graph.add_edge(edge.source, edge.destination, edge.cost)

    shortest_paths = dijkstra(graph, vertices[0])

    print("Vertex | Cost | Path")
    print("---------------------")
    for vertex in shortest_paths:
        path = reconstruct_path(vertex)
        print(f"  {vertex.label}    | {vertex.cost:4} | {' -> '.join(map(str, path))}")