

## Using DFS 
Parent is used for undirected graph to check if the node visited again is not from its children
```python
from collections import defaultdict

class Graph:
    def __init__(self, vertices):
        self.graph = defaultdict(list)
        self.V = vertices

    def add_edge(self, u, v):
        self.graph[u].append(v)

    def is_cyclic_util(self, v, visited, parent):
        visited[v] = True
        for i in self.graph[v]:
            if not visited[i]:
                if self.is_cyclic_util(i, visited, v):
                    return True
            elif parent != i:
                return True
        return False

    def has_cycle(self):
        visited = [False] * self.V
        for i in range(self.V):
            if not visited[i]:
                if self.is_cyclic_util(i, visited, -1):
                    return True
        return False

# Example usage:
g = Graph(4)
g.add_edge(0, 1)
g.add_edge(1, 2)
g.add_edge(2, 0)
g.add_edge(2, 3)

if g.has_cycle():
    print("The graph has a cycle.")
else:
    print("The graph does not have a cycle.")
```


## Using BFS 

```python
from collections import defaultdict, deque

class Graph:
    def __init__(self, vertices):
        self.graph = defaultdict(list)
        self.V = vertices

    def add_edge(self, u, v):
        self.graph[u].append(v)
        self.graph[v].append(u)  # For undirected graph, add the reverse edge.

    def has_cycle(self):
        visited = [False] * self.V
        for i in range(self.V):
            if not visited[i]:
                if self.is_cyclic_util(i, visited):
                    return True
        return False

    def is_cyclic_util(self, v, visited):
        queue = deque()
        visited[v] = True
        queue.append((v, -1))  # Tuple (node, parent)

        while queue:
            current, parent = queue.popleft()

            for neighbor in self.graph[current]:
                if not visited[neighbor]:
                    visited[neighbor] = True
                    queue.append((neighbor, current))
                elif parent != neighbor:
                    return True  # Cycle detected

        return False

# Example usage:
g = Graph(4)
g.add_edge(0, 1)
g.add_edge(1, 2)
g.add_edge(2, 0)
g.add_edge(2, 3)

if g.has_cycle():
    print("The graph has a cycle.")
else:
    print("The graph does not have a cycle.")

```


## Using Union-Find Algorithm

- Initialize each vertex as a separate set (Make Set operation).
- Iterate through the edges of the graph. For each edge (u, v):
    - Find the representative (leader) of the set containing vertex u (Find operation).
    - Find the representative (leader) of the set containing vertex v (Find operation).
    - If both vertices have the same leader, it means they belong to the same set, and adding this edge would create a cycle. In this case, you have detected a cycle.
- Otherwise, merge the sets of u and v by performing a Union operation.
- Continue this process for all edges. If you encounter any edge that would connect two vertices already in the same set, it indicates the presence of a cycle.

```python
class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
    
    def find(self, x):
        if self.parent[x] == x:
            return x
        self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
    
    def union(self, x, y):
        root_x = self.find(x)
        root_y = self.find(y)
        if root_x != root_y:
            self.parent[root_x] = root_y

def has_cycle(graph):
    n = len(graph)
    uf = UnionFind(n)
    
    for u, v in graph:
        if uf.find(u) == uf.find(v):
            return True
        uf.union(u, v)
    
    return False

# Example usage:
edges = [(0, 1), (1, 2), (2, 0), (2, 3)]
if has_cycle(edges):
    print("The graph has a cycle.")
else:
    print("The graph does not have a cycle.")

```

## Using DFS for Directed graph 

For directed graph, instead of single parent, we need to keep track of all nodes in that cycle
```python 
from collections import defaultdict

class Graph:
    def __init__(self, vertices):
        self.graph = defaultdict(list)
        self.V = vertices

    def add_edge(self, u, v):
        self.graph[u].append(v)

    def has_cycle(self):
        visited = [False] * self.V
        recursion_stack = [False] * self.V  # To keep track of nodes in the current DFS path.

        for i in range(self.V):
            if not visited[i]:
                if self.is_cyclic_util(i, visited, recursion_stack):
                    return True
        return False

    def is_cyclic_util(self, v, visited, recursion_stack):
        visited[v] = True
        recursion_stack[v] = True

        for neighbor in self.graph[v]:
            if not visited[neighbor]:
                if self.is_cyclic_util(neighbor, visited, recursion_stack):
                    return True
            elif recursion_stack[neighbor]:
                return True

        recursion_stack[v] = False
        return False

# Example usage:
g = Graph(4)
g.add_edge(0, 1)
g.add_edge(1, 2)
g.add_edge(2, 0)
g.add_edge(2, 3)

if g.has_cycle():
    print("The directed graph has a cycle.")
else:
    print("The directed graph does not have a cycle.")

```