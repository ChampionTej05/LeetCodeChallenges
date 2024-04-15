
from collections import defaultdict
class Graph:
    
    def __init__(self) :
        self.graph = defaultdict(set)
        
        
    def add_edge(self, src, dest):
        self.graph[src].add(dest)
        self.graph[dest].add(src)
        
    def DFS(self, node, visited):
        visited[node] = True 
        print(" ", node, end = '->')
        for neighbour in self.graph[node]:
            if not visited[neighbour]:
                self.DFS(neighbour, visited)
        
        
    def traverse_dfs(self, start_node_index):
        visited = [False]*len(self.graph)
        
        self.DFS(start_node_index, visited)
        
    def traverse_bfs(self, start_node_index):
        
        from collections import deque 
        queue = deque()
        visited = [False]*len(self.graph)
        visited[start_node_index]=True 
        queue.append(start_node_index)        
        while queue:
            
            node = queue.popleft()
            print(" ", node, end = '->')
            for neighbour in self.graph[node]:
                if not visited[neighbour]:
                    queue.append(neighbour)
                    visited[neighbour]=True 
                    
    def level_of_graph(self,start_node_index):
        from collections import deque 
        
        queue = deque()
        queue.append(start_node_index)
        visited = [False]*len(self.graph)
        level = 0 
        while queue:
            
            length_of_queue = len(queue)
            for i in range(length_of_queue):
                #pop all nodes and put their children inside if not visited 
                node = queue.popleft() 
                for neighbour in self.graph[node]:
                    if not visited[neighbour]:
                        queue.append(neighbour)
                        visited[neighbour]=True 
                        
            level+=1 
            
        print("level: ", level)
                    
        
        
        

    @staticmethod    
    def build_graph():
        graph = Graph()
        graph.add_edge(0,1)
        graph.add_edge(1,3)
        graph.add_edge(1,2)
        graph.add_edge(1,4)
        graph.add_edge(1,5)
        graph.add_edge(2,5)
        graph.add_edge(5,6)
        return graph
        
 
    
    

graph = Graph.build_graph()
# graph.traverse_dfs(0)
# graph.traverse_bfs(0)
graph.level_of_graph(0)
        
                