'''
Here the order is asked 
'''

class Graph:
    
    def __init__(self):
        # adjacency list method 
        self.graph = {}

    def init_adjancency_list_for_nodes(self,nodes):
        for node in nodes:
            self.graph[node] = []

    def add_edge(self, source, destination):

        if source in self.graph:
            self.graph[source].append(destination)
        else:
            self.graph[source] = [destination]

    #not needed
    def get_source_nodes(self):

        visited_nodes = set()

        for values in self.graph.values():
            for destination in values:
                visited_nodes.add(destination)

        
        source_nodes = [ nodes for nodes in list(self.graph.keys()) if nodes not in visited_nodes]
        
        return source_nodes
    
    def has_cycle(self, source , visited, recursion_stack):

        # intially mark current source as visited and having cycle 
        visited[source] = True 
        recursion_stack[source] = True 

        for neighbour in self.graph[source]:
            #if the neighbour is not visited already, explore it 

            if not visited[neighbour]:
                #explore it 
                if self.has_cycle(neighbour, visited, recursion_stack):
                    return True
            else:
                #node has been explored in the past but it could have cycle originating from it (backtrackign type solution)
                if recursion_stack[neighbour]:
                    return True 
                
        # all neighbours explored, no cycle found 
        recursion_stack[source] = False
        return False
    
    def check_if_forest_has_cycle(self, numNodes):
        visited = [False] * numNodes
        recursion_stack = [False] * numNodes

        for source in range(numNodes):
            if not visited[source]:
                if self.has_cycle(source, visited, recursion_stack):
                    return True, None 
        

        # find courses order for each node 
        visited = [False] * numNodes
        courses_order = []
        for node in range(numNodes):
            if not visited[node]:
                self.traverse_nodes(node, visited, courses_order)

        return False, courses_order
    def traverse_nodes(self,source, visited, courses_order):
        visited[source] = True
        if source in self.graph:
            for neighbour in self.graph[source]:
                if not visited[neighbour]:
                    self.traverse_nodes(neighbour, visited, courses_order)

        courses_order.append(source)


class Solution(object):
    def findOrder(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: List[int]
        """
        forest = Graph()
        forest.init_adjancency_list_for_nodes(range(numCourses))
        for source , destination in prerequisites:
            forest.add_edge(source, destination)

        has_cycle, courses_order = forest.check_if_forest_has_cycle(numCourses)
        if has_cycle:
            return []
        else:
            return courses_order



        