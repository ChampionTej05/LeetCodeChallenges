'''
https://leetcode.com/problems/amount-of-time-for-binary-tree-to-be-infected/description/

1. Convert the Tree into undirected graph 
2. Consider the infected node as the Starting point of the BFS
3. Perform level order traversal 
4. Return the levels 
'''

from collections import defaultdict
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class UndirectedGraph:

    def __init__(self):
        self.root = None 
        self.graph = defaultdict(list)


    def add_edge(self, source, destination):
        self.graph[source].append(destination)
        self.graph[destination].append(source)

    
    def build_graph_from_tree(self, tree:TreeNode):

        if tree is None:
            return 
        
        # consider root and left child 

        if tree.left is not None:
            self.add_edge(tree.val, tree.left.val)

        # consider root and right child 
            
        if tree.right is not None:
            self.add_edge(tree.val, tree.right.val)

        # recur the process for left and right child 
            
        self.build_graph_from_tree(tree.left)
        self.build_graph_from_tree(tree.right)

    def level_order(self, start):

        from collections import deque

        queue = deque()
        queue.append(start)

        level = 0 
        while queue:

            queue_length = len(queue)
            
            for i in range(queue_length):
                node = queue.popleft()
                print("node : ", node)

                for neighbour in self.graph[node]:
                    if self.graph[neighbour]:
                        queue.append(neighbour)

                # mark this node as visited
                self.graph[node] = False
            level+=1

        # off-by-1 error
        return level-1 if level>0 else 0




graph = UndirectedGraph()
# root = [1,5,3,null,4,10,6,9,2]
# start = 3

root  = TreeNode()
start  = 0

graph.build_graph_from_tree(root)
level = graph.level_order(start)