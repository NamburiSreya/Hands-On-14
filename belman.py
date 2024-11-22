class Edge:
    def __init__(self, from_node, to_node, cost):
        self.from_node = from_node
        self.to_node = to_node
        self.cost = cost

class Vertex:
    def __init__(self, label):
        self.label = label
        self.distance = float('inf')
        self.parent = None

def relax_edge(u, v, weight):
    if v.distance > u.distance + weight:
        v.distance = u.distance + weight
        v.parent = u

def init_single_source(graph, start):
    for vertex in graph.vertices:
        vertex.distance = float('inf')
        vertex.parent = None
    start.distance = 0

def bellman_ford(graph, start):
    init_single_source(graph, start)
    for _ in range(len(graph.vertices) - 1):
        for (u, v), weight in graph.edges.items():
            relax_edge(u, v, weight)
    
    # Check for negative-weight cycles
    for (u, v), weight in graph.edges.items():
        if v.distance > u.distance + weight:
            return False  # Negative-weight cycle detected
    return True

class Graph:
    def __init__(self, vertices):
        self.vertices = vertices
        self.adjacency = {v: [] for v in vertices}
        self.edges = {}

    def add_edge(self, from_node, to_node, cost):
        self.adjacency[from_node].append(to_node)
        self.edges[(from_node, to_node)] = cost

    def __str__(self):
        result = "\n--- Adjacent Vertices ---\n"
        for vertex, neighbors in self.adjacency.items():
            result += f"{vertex.label}: {' '.join(str(v.label) for v in neighbors)}\n"
        return result + "--- End of Adjacent Vertices ---\n"

if __name__ == "__main__":
    # Example from figure 24.4 of Chapter 24 of 2009 Introduction to Algorithms by Cormen et al.
    # s: 0, t: 1, x: 2, y: 3, z: 4

    vertices = [Vertex(i) for i in range(5)]

    edges = [Edge(vertices[0], vertices[1], 6),
             Edge(vertices[0], vertices[3], 7),
             Edge(vertices[1], vertices[2], 5),
             Edge(vertices[1], vertices[3], 8),
             Edge(vertices[1], vertices[4], -4),
             Edge(vertices[2], vertices[1], -2),
             Edge(vertices[3], vertices[2], -3),
             Edge(vertices[3], vertices[4], 9),
             Edge(vertices[4], vertices[0], 2),
             Edge(vertices[4], vertices[2], 7)]

    graph = Graph(vertices)
    for edge in edges:
        graph.add_edge(edge.from_node, edge.to_node, edge.cost)

    print(graph)
    print("Number of edges:", len(graph.edges))

    no_negative_cycle = bellman_ford(graph, vertices[0])
    print("No negative-weight cycle:" if no_negative_cycle else "Negative-weight cycle detected")

    if no_negative_cycle:
        print("\nShortest paths from vertex 0:")
        for v in vertices:
            path = []
            current = v
            while current:
                path.append(str(current.label))
                current = current.parent
            path.reverse()
            print(f"To {v.label}: Distance = {v.distance}, Path = {' -> '.join(path)}")

#output

#--- Adjacent Vertices ---
0: 1 3
1: 2 3 4
2: 1
3: 2 4
4: 0 2
#--- End of Adjacent Vertices ---

#Number of edges: 10
#No negative-weight cycle:

#Shortest paths from vertex 0:
#To 0: Distance = 0, Path = 0
#To 1: Distance = 2, Path = 0 -> 3 -> 2 -> 1
#To 2: Distance = 4, Path = 0 -> 3 -> 2
#To 3: Distance = 7, Path = 0 -> 3
#To 4: Distance = -2, Path = 0 -> 3 -> 2 -> 1 -> 4
