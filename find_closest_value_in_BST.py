def findClosestValueInBst(tree, target):
    # Write your code here.
    # a = traverse_inorder_iterative_BST_modified(tree, target)
    # sorted_result = sorted(a, key = lambda a: a[0])
    
    # print(a)
    # print(sorted_result)
    # return sorted_result[0][1]


    # a= traverse_inorder_iterative_BST_modified_with_global_sum(tree, target)
    # print(a.value)
    # return a.value 

    a = helper_function(tree, target, tree)
    print(a.value)
    return a.value




def traverse_inorder_iterative_BST(tree):

    stack, result= [], []
    current = tree #root node

    while True:
        #append on left nodes till we reach child node
        while current is not None:
            stack.append(current)
            current = current.left 

        if not stack:
            return result
        
        # take current node's value
        current = stack.pop()
        result.append(current.value)
        #traverse right side now 
        current = current.right 
 
def traverse_inorder_iterative_BST_modified(tree, target):
    
    stack, result= [], []
    current = tree #root node

    while True:
        #append on left nodes till we reach child node
        while current is not None:
            stack.append(current)
            current = current.left 

        if not stack:
            return result
        
        # take current node's value
        current = stack.pop()
        #store node and it's abs value with target 
        result.append([abs(current.value-target),current.value])
        #traverse right side now 
        current = current.right 

def traverse_inorder_iterative_BST_modified_with_global_sum(tree, target):
    
    stack, result= [], []
    import sys
    min_difference = sys.maxsize# this is the minimum difference we are looking for in the tree 
    current = tree #root node
    min_difference_node = tree

    while True:
        #append on left nodes till we reach child node
        while current is not None:
            stack.append(current)
            current = current.left 

        if not stack:
            return min_difference_node
        
        # take current node's value
        current = stack.pop()
        #store node and it's abs value with target 
        current_diff = abs(current.value-target)
        if current_diff < min_difference:
            min_difference = current_diff
            min_difference_node = current 
        #traverse right side now 
        current = current.right 

#most optimised O(log(nodes))
def helper_function(tree, target, closest_node):
    if tree is None:
        return closest_node
    
    current_dist = tree.value - target 
    if abs(closest_node.value - target) > abs(current_dist):
        closest_node = tree 

    if current_dist > 0:
        #we will get all big difference values on right side than current node value 
        return helper_function(tree.left, target, closest_node)
    elif current_dist <0:
        return helper_function(tree.right, target, closest_node)
    else:
        return closest_node
    
    
# This is the class of the input tree. Do not edit.
class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def __str__(self) -> str:
        return " " + self.value + " "


# This file is initialized with a code version of this
# question's sample test case. Feel free to add, edit,
# or remove test cases in this file as you see fit!


import unittest


class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class TestProgram(unittest.TestCase):
    def test_case_1(self):
        root = BST(10)
        root.left = BST(5)
        root.left.left = BST(2)
        root.left.left.left = BST(1)
        root.left.right = BST(5)
        root.right = BST(15)
        root.right.left = BST(13)
        root.right.left.right = BST(14)
        root.right.right = BST(22)
        expected = 13
        actual = findClosestValueInBst(root, 12)
        self.assertEqual(expected, actual)


obj = TestProgram()
obj.test_case_1()


