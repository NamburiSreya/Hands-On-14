Graph Algorithm Implementations

This project implements three fundamental graph algorithms: Dijkstra's algorithm, the Bellman-Ford algorithm, and the Floyd-Warshall algorithm. These algorithms are used to solve shortest path problems in weighted graphs.

Dijkstra's Algorithm
Dijkstra's algorithm finds the shortest path from a single source vertex to all other vertices in a weighted graph with non-negative edge weights.
Features:
Single-source shortest path calculation
Efficient for graphs with non-negative edge weights
Implementation using a priority queue (simulated with a list in this version)

Bellman-Ford Algorithm
The Bellman-Ford algorithm finds the shortest paths from a single source vertex to all other vertices in a weighted graph, allowing for negative edge weights.
Features:
Single-source shortest path calculation
Handles graphs with negative edge weights
Detects negative-weight cycles

Floyd-Warshall Algorithm
The Floyd-Warshall algorithm finds the shortest paths between all pairs of vertices in a weighted graph.
Features:
All-pairs shortest path calculation
Handles graphs with negative edge weights (but no negative cycles)
Includes both iterative and recursive implementations
Generates a predecessor matrix for path reconstruction
