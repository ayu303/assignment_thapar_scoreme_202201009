
### 2. `main.py`


"""
Assignment: Implement the most efficient algorithm to solve the given problem.

Problem Statement:
You are given a Directed Acyclic Graph (DAG) with `n` nodes, numbered from `0` to `n-1`.
The graph is represented as an adjacency list where `graph[i]` is a list of tuples `(j, w)`,
representing an edge from node `i` to node `j` with weight `w`. Your task is to find the longest
path in the graph starting from any node.

Function Signature:
def longest_path(graph: list) -> int:

Parameters:
- graph (list): A list of lists, where `graph[i]` contains tuples `(j, w)` representing an edge
  from node `i` to node `j` with weight `w`.

Returns:
- int: The length of the longest path in the graph.

Example:
>>> graph = [
...     [(1, 3), (2, 2)],
...     [(3, 4)],
...     [(3, 1)],
...     []
... ]
>>> longest_path(graph)
7
"""

def longest_path(graph: list) -> int:
    def topological_sort(graph):
        n = len(graph)
        visited = [False] * n
        topo_order=[]

        def dfs(node):
            visited[node] = True
            for neighbour, _ in graph[node]:
                if not visited[neighbour]:
                    dfs(neighbour)
            topo_order.append(node)

        for i in range(n):
            if not visited[i]:
                dfs(i)
        topo_order.reverse()
        return topo_order
    
    def calculate_longest_path(graph, topo_order):
     n=len(graph)
     dist = [-float('inf')] * n

     in_degree= [0] * n
     for node in range(n):
         for neighbor, _ in graph[node]:
             in_degree[neighbor] += 1

     for i in range(n):
         if in_degree[i] == 0:
             dist[i]=0

     for node in topo_order:
        if dist[node] != -float('inf'):
            for neighbour, weight in graph[node]:
                if dist[neighbour] < dist[node] + weight:
                    dist[neighbour] = dist[node] + weight
     return max(dist)
    topo_order=topological_sort(graph)
    return calculate_longest_path(graph, topo_order)
