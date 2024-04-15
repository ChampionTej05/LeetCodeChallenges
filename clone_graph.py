'''
https://leetcode.com/problems/clone-graph/description/

Using DFS 
    1. We store the nodes which have cloned 
    2. Everytime we visit the node, we check 
        a. If it is cloned --> add it as neighbour to parent node 
        b. If not cloned --> run DFS and then add it as neighbour to parent node 
'''


"""
# Definition for a Node.

"""
class Node(object):
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

    def __repr__(self) -> str:
        return str(self.val)

class Solution(object):
    def DFS(self, node, cloned_nodes):

        if not node:
            return node 
        
        if node.val not in cloned_nodes:
            cloned_nodes[node.val] = Node(node.val)
        else:
            return cloned_nodes[node.val]
        
        cloned_neighbours = []
        for neighbor in node.neighbors:
            if neighbor.val in cloned_nodes:
                cloned_neighbours.append(cloned_nodes[neighbor.val])
            else:
                cloned_neighbours.append(self.DFS(neighbor, cloned_nodes))

        
        cloned_nodes[node.val].neighbors = cloned_neighbours

        return cloned_nodes[node.val]

    def cloneGraph(self, node):
        """
        :type node: Node
        :rtype: Node
        """

        cloned_nodes = {}
        clone_head = self.DFS(node, cloned_nodes)
        return clone_head


node1 = Node(1)
node2 = Node(2)
node3 = Node(3)
node4 = Node(4)

node1.neighbors.extend([node2,node4])
node2.neighbors.extend([node1,node3])
node3.neighbors.extend([node2, node4])
node4.neighbors.extend([node1, node3])

obj = Solution()
cloned_head = obj.cloneGraph(node1)
print(cloned_head.val, cloned_head.neighbors)
if cloned_head.neighbors == node1.neighbors:
    print("Worked")