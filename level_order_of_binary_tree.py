'''
Level order traversal of Binary Tree 

leetcode: https://leetcode.com/problems/binary-tree-level-order-traversal/description/ 
'''
class TreeNode:
    def __init__(self, value=0, left=None, right=None):
        self.val = value
        self.left = left
        self.right = right

def levelOrder_v1(root):
    from collections import deque

    queue = deque()
    results = []

    if root is None:
        return results 
    
    queue.append(root)

    while len(queue) >0:

        current_level_nodes = []
        #run to the original length of queue
        for i in range(len(queue)):
            node = queue.popleft()
            if node:
                current_level_nodes.append(node.val)
                childrens = []
                if node.left:
                    childrens.append(node.left)
                if node.right:
                    childrens.append(node.right)

                queue.extend(childrens)

        if len(current_level_nodes)>0:
            results.append(current_level_nodes)
            

    print(results)
    return results 

def levelOrder(root):
    from collections import deque 

    queue = deque()
    results = []

    if root is None:
        return results 
    
    queue.append(root)
    # results.append([root.val])

    while len(queue)>0:
        
        current_level_nodes_value = [] 
        current_level_nodes = []
        while queue:
            node = queue.popleft()
            current_level_nodes_value.append(node.val)
            current_level_nodes.append(node)

        if len(current_level_nodes)>0:
            results.append(current_level_nodes_value)
            for node in current_level_nodes:
                if node.left :
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        
    print(results)
    return results


import unittest

class TestLevelOrderTraversal(unittest.TestCase):
    
    def buildTree(self, nodes):
        if not nodes:
            return None
        root = TreeNode(nodes[0])
        queue = [root]
        index = 1
        while queue and index < len(nodes):
            node = queue.pop(0)
            if nodes[index] is not None:
                node.left = TreeNode(nodes[index])
                queue.append(node.left)
            index += 1

            if index < len(nodes) and nodes[index] is not None:
                node.right = TreeNode(nodes[index])
                queue.append(node.right)
            index += 1
        return root

    def test_level_order(self):
        # Test case 1
        tree = self.buildTree([3, 9, 20, None, None, 15, 7])
        self.assertEqual(levelOrder(tree), [[3], [9, 20], [15, 7]])

        # Test case 2
        tree = self.buildTree([1])
        self.assertEqual(levelOrder(tree), [[1]])

        # Test case 3
        tree = self.buildTree([])
        self.assertEqual(levelOrder(tree), [])

        # test case 4 
        tree = self.buildTree([1, 2, 3,4,5 , None, None])
        self.assertEqual(levelOrder(tree), [[1],[2,3],[4,5]])

if __name__ == '__main__':
    unittest.main()




