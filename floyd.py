from typing import List
import numpy as np

def floyd_warshall(adjacency_matrix: List[List[float]]) -> np.ndarray:
    """
    Implements the Floyd-Warshall algorithm for all-pairs shortest paths.
    """
    dist = np.array(adjacency_matrix, dtype=float)
    n = len(dist)
    
    for k in range(n):
        for i in range(n):
            for j in range(n):
                dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])
        
        print(f"\nDistance matrix after considering vertex {k}:")
        print(dist)
    
    return dist

def floyd_warshall_recursive(adjacency_matrix: np.ndarray, k: int) -> np.ndarray:
    """
    Recursive implementation of the Floyd-Warshall algorithm.
    """
    if k == len(adjacency_matrix):
        return adjacency_matrix
    
    dist = adjacency_matrix.copy()
    for i in range(len(dist)):
        for j in range(len(dist)):
            dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])
    
    print(f"\nDistance matrix after considering vertex {k}:")
    print(dist)
    
    return floyd_warshall_recursive(dist, k + 1)

def initialize_predecessor_matrix(adjacency_matrix: List[List[float]]) -> np.ndarray:
    """
    Initializes the predecessor matrix for path reconstruction.
    """
    n = len(adjacency_matrix)
    pred = np.full((n, n), -1, dtype=int)
    
    for i in range(n):
        for j in range(n):
            if i != j and adjacency_matrix[i][j] != float('inf'):
                pred[i][j] = i
    
    return pred

if __name__ == "__main__":
    # Example from figure 25.4 of Chapter 25 of 2009 Introduction to Algorithms by Cormen et al.
    infinity = float('inf')
    graph = [
        [0, 3, 8, infinity, -4],
        [infinity, 0, infinity, 1, 7],
        [infinity, 4, 0, infinity, infinity],
        [2, infinity, -5, 0, infinity],
        [infinity, infinity, infinity, 6, 0]
    ]

    print("Standard Floyd-Warshall Algorithm:")
    final_distances = floyd_warshall(graph)
    print("\nFinal distance matrix:")
    print(final_distances)

    print("\nRecursive Floyd-Warshall Algorithm:")
    final_distances_recursive = floyd_warshall_recursive(np.array(graph), 0)
    print("\nFinal distance matrix (recursive):")
    print(final_distances_recursive)

    print("\nInitial Predecessor Matrix:")
    predecessor_matrix = initialize_predecessor_matrix(graph)
    print(predecessor_matrix)
#Standard Floyd-Warshall Algorithm:

#Distance matrix after considering vertex 0:
[[ 0.  3.  8. inf -4.]
 [inf  0. inf  1.  7.]
 [inf  4.  0. inf inf]
 [ 2.  5. -5.  0. -2.]
 [inf inf inf  6.  0.]]

#Distance matrix after considering vertex 1:
[[ 0.  3.  8.  4. -4.]
 [inf  0. inf  1.  7.]
 [inf  4.  0.  5. 11.]
 [ 2.  5. -5.  0. -2.]
 [inf inf inf  6.  0.]]

#Distance matrix after considering vertex 2:
[[ 0.  3.  8.  4. -4.]
 [inf  0. inf  1.  7.]
 [inf  4.  0.  5. 11.]
 [ 2. -1. -5.  0. -2.]
 [inf inf inf  6.  0.]]

#Distance matrix after considering vertex 3:
[[ 0.  3. -1.  4. -4.]
 [ 3.  0. -4.  1. -1.]
 [ 7.  4.  0.  5.  3.]
 [ 2. -1. -5.  0. -2.]
 [ 8.  5.  1.  6.  0.]]

#Distance matrix after considering vertex 4:
[[ 0.  1. -3.  2. -4.]
 [ 3.  0. -4.  1. -1.]
 [ 7.  4.  0.  5.  3.]
 [ 2. -1. -5.  0. -2.]
 [ 8.  5.  1.  6.  0.]]

#Final distance matrix:
[[ 0.  1. -3.  2. -4.]
 [ 3.  0. -4.  1. -1.]
 [ 7.  4.  0.  5.  3.]
 [ 2. -1. -5.  0. -2.]
 [ 8.  5.  1.  6.  0.]]

#Recursive Floyd-Warshall Algorithm:

#Distance matrix after considering vertex 0:
[[ 0.  3.  8. inf -4.]
 [inf  0. inf  1.  7.]
 [inf  4.  0. inf inf]
 [ 2.  5. -5.  0. -2.]
 [inf inf inf  6.  0.]]

#Distance matrix after considering vertex 1:
[[ 0.  3.  8.  4. -4.]
 [inf  0. inf  1.  7.]
 [inf  4.  0.  5. 11.]
 [ 2.  5. -5.  0. -2.]
 [inf inf inf  6.  0.]]

#Distance matrix after considering vertex 2:
[[ 0.  3.  8.  4. -4.]
 [inf  0. inf  1.  7.]
 [inf  4.  0.  5. 11.]
 [ 2. -1. -5.  0. -2.]
 [inf inf inf  6.  0.]]

#Distance matrix after considering vertex 3:
[[ 0.  3. -1.  4. -4.]
 [ 3.  0. -4.  1. -1.]
 [ 7.  4.  0.  5.  3.]
 [ 2. -1. -5.  0. -2.]
 [ 8.  5.  1.  6.  0.]]

#Distance matrix after considering vertex 4:
[[ 0.  1. -3.  2. -4.]
 [ 3.  0. -4.  1. -1.]
 [ 7.  4.  0.  5.  3.]
 [ 2. -1. -5.  0. -2.]
 [ 8.  5.  1.  6.  0.]]

#Final distance matrix (recursive):
[[ 0.  1. -3.  2. -4.]
 [ 3.  0. -4.  1. -1.]
 [ 7.  4.  0.  5.  3.]
 [ 2. -1. -5.  0. -2.]
 [ 8.  5.  1.  6.  0.]]

#Initial Predecessor Matrix:
[[-1  0  0 -1  0]
 [-1 -1 -1  1  1]
 [-1  2 -1 -1 -1]
 [ 3 -1  3 -1 -1]
 [-1 -1 -1  4 -1]]