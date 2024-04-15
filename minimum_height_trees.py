'''
https://leetcode.com/problems/minimum-height-trees/description/
'''
'''
Why Your Approach is Inefficient
Repeated BFS: For each node, you're performing a BFS to determine the height of the tree rooted at that node. This operation is costly and is repeated for every node.
Overhead in Level Calculation: Your level calculation involves a nested loop and a queue, which adds to the time complexity.
Improvement: Using the Concept of Leaves
A more efficient approach is to trim the leaves iteratively. A leaf is a node with only one connection. The idea is that the root of an MHT will be towards the center of the graph. By trimming the leaves level by level, you are effectively moving towards the center.

Here's a brief overview of the improved algorithm:

Initialize: Start by putting all the leaves (nodes with only one connection) into a queue.
Trimming Process:
In each iteration, remove the leaves from the queue and also remove the edges associated with them.
After removing the leaves, some of the nodes will become new leaves. Add these new leaves to the queue for the next iteration.
Continue this process until there are 1 or 2 nodes left in the graph (depending on the graph's structure). These nodes are the roots of the MHTs.
Efficiency: This method significantly reduces the number of operations compared to the BFS approach for every node.

'''
class Graph:

    def __init__(self, nodes) :
        self.graph = {}
        self.nodes = nodes
        for node in nodes:
            self.graph[node] = []

    def add_edge(self, source, destination):
        self.graph[source].append(destination)
        self.graph[destination].append(source)
    
    def get_children(self, node):
        if node in self.graph:
            return self.graph[node]
    
        return None 
    
    def level_of_graph(self, source):
        level = 0 
        from collections import deque 
        queue = deque()
        queue.append(source)
        visited = [False]* len(self.graph.keys())

        while queue:
            
            nodes = []

            #empty complete queue of this level 
            while queue:
                node = queue.popleft()
                visited[node] = True 
                nodes.append(node)

            for node in nodes:
                for children in self.get_children(node):
                    if not visited[children]:
                        queue.append(children)
            level+=1

            print("Queue State: {}".format(queue))
            print(" ---- ")
        
        return level
    
    def build_graph(self,edges):
        for source, destination in edges:
            self.add_edge(source, destination)

    #brute force method 
    def give_minimum_height_trees(self,nodes):
        
        mapper = {}
        minLevel = len(nodes)+1
        for node in nodes:
            
            level = self.level_of_graph(node)
            print("Root : {}, level : {}".format(node, level))
            if level <= minLevel:
                minLevel = level 
            if level in mapper:
                mapper[level].append(node)
            else:
                mapper[level]= [node]
        
        min_nodes = mapper[minLevel]
        return min_nodes
    
from collections import defaultdict, deque

def findMinHeightTrees(n, edges):
    if n <= 2:
        return [i for i in range(n)]

    neighbors = defaultdict(set)
    for start, end in edges:
        neighbors[start].add(end)
        neighbors[end].add(start)

    leaves = deque([i for i in range(n) if len(neighbors[i]) == 1])

    remaining_nodes = n
    while remaining_nodes > 2:
        leaves_count = len(leaves)
        remaining_nodes -= leaves_count

        for _ in range(leaves_count):
            leaf = leaves.popleft()
            for neighbor in neighbors[leaf]:
                neighbors[neighbor].remove(leaf)
                if len(neighbors[neighbor]) == 1:
                    leaves.append(neighbor)
    
    return list(leaves)

# Example usage
n = 6
edges = [[0,1],[0,2],[0,3],[3,4],[4,5]]
print(findMinHeightTrees(n, edges))


n = 6
edges = [[0,1],[0,2],[0,3],[3,4],[4,5]]
nodes = range(n)
graph = Graph(nodes)
graph.build_graph(edges)

# print(graph.level_of_graph(1))

print(graph.give_minimum_height_trees(nodes))