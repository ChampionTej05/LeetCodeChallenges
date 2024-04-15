'''
LEETCODE: https://leetcode.com/problems/course-schedule/    

Approach:
We will represent this problem as disconnected graph (forest)

We will use modified DFS Traversal to find the solution 
visited --> this will help us , to check whether to again explore the children 
recursion_stack --> this stores whether for current vertex there is cycle orginating from it or not 
This recursion_stack will help us while we are in DFS search from current vertex 
'''
'''

ex: A->B->C->D and X->Y->Z->C->D 

in this example above, visited array only would give cycle as we have visited it in past but actually it is not cycle 
which is decided only using recursion stack 
-------
Why is Cycle Detection Needed?
In the Course Schedule problem, you are essentially asked if you can finish all courses given the prerequisites for each course. This problem can be modeled as a graph where each course is a node, and a directed edge from node A to node B signifies that course A is a prerequisite for course B.

The critical point here is that if the graph contains a cycle, it implies that there are circular dependencies among some courses, making it impossible to complete all courses. Hence, cycle detection is crucial to solving this problem.

Why Use a Recursion Stack?
The use of a recursion stack, in addition to the visited array, is necessary for detecting cycles in a directed graph. Here's why:

Visited Array: The visited array keeps track of the nodes that have been visited in the graph traversal. Once a node is visited, it is marked true in this array.
Recursion Stack: This is a more nuanced tool. It not only tracks whether a node has been visited, but also whether the node is part of the current path being explored. In other words, the recursion stack tracks the ancestry of the node in the current depth-first search (DFS) traversal.
When you visit a node, you mark it true in both the visited array and the recursion stack.
When you leave a node (i.e., you've explored all its neighbors), you mark it false in the recursion stack (but it remains true in the visited array).
If you encounter a node that is already in the recursion stack (i.e., it's true in the recursion stack), it means you've found a cycle. This is because you've reached a node that is already part of the current path you're exploring.
Why Can't We Just Use Visited?
If you use only the visited array, you lose the ability to differentiate between a node that was visited in the current path (and thus potentially part of a cycle) and a node that was visited in a previous path (and thus not indicative of a cycle in the current path). The recursion stack provides this context, which is critical for cycle detection in directed graphs.

In summary, the recursion stack in your solution is used to track the path being explored in the current DFS traversal. This is crucial for detecting cycles, which is essential for solving the Course Schedule problem. Without the recursion stack, you might incorrectly identify a node as part of a cycle just because it was visited in a different DFS traversal.
'''

class Graph:
    
    def __init__(self) -> None:
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
                    return True 
        
        return False 
    
def canFinish(numCourses, prerequisites):
    forest = Graph()
    forest.init_adjancency_list_for_nodes(range(numCourses))
    for source , destination in prerequisites:
        forest.add_edge(source, destination)

    return not forest.check_if_forest_has_cycle(numCourses)


# Example 1: No cycles, all courses can be finished
numCourses1 = 4
prerequisites1 = [[1, 0], [2, 1], [3, 2]]
print(canFinish(numCourses1, prerequisites1))  # True

# Example 2: Cycle present, impossible to finish all courses
numCourses2 = 3
prerequisites2 = [[0, 1], [1, 2], [2, 0]]
print(canFinish(numCourses2, prerequisites2))  # False

# Example 3: No prerequisites, all courses can be finished
numCourses3 = 5
prerequisites3 = []
print(canFinish(numCourses3, prerequisites3))  # True

# Example 4: Multiple disconnected components, all courses can be finished
numCourses4 = 6
prerequisites4 = [[1, 0], [2, 1], [3, 2], [5, 4]]
print(canFinish(numCourses4, prerequisites4))  # True

# Example 5: Large graph with cycles, impossible to finish all courses
numCourses5 = 100
prerequisites5 = [[i, i + 1] for i in range(99)] + [[99, 0]]
print(canFinish(numCourses5, prerequisites5))  # False


# # Create an instance of the Graph class
# forest = Graph()

# nodes = ['A','B','C','D','X','Y','Z','1','2','3','4','M','N','O','P','Q']
# forest.init_adjancency_list_for_nodes(nodes)
# # Add edges to the first disconnected component (Graph 1)
# forest.add_edge('A', 'B')
# forest.add_edge('B', 'C')
# forest.add_edge('C', 'D')
# forest.add_edge('X', 'Y')
# forest.add_edge('Y', 'Z')
# # forest.add_edge('D','A')

# # Add edges to the second disconnected component (Graph 2)
# forest.add_edge('1', '2')
# forest.add_edge('2', '3')
# forest.add_edge('3', '4')

# # Add edges to the third disconnected component (Graph 3)
# forest.add_edge('M', 'N')
# forest.add_edge('N', 'O')
# forest.add_edge('P', 'Q')

# sources = forest.get_source_nodes()

# print(forest.check_forest())