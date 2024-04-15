class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert(self, value):
        # Write your code here.
        # Do not edit the return statement of this method.

        # self.insert_iterative(value)
        node = BST(value)
        if self is None:
            
            return node 
        

        if self.value > value:
            self.left = self.left.insert(value) if self.left else node
        else:
            self.right = self.right.insert(value) if self.right else node
        return self
    
    def insert_iterative(self, value):
        current, parent = self, self 
        while current:
            if current.value > value:
                parent = current 
                current = current.left 
            else:
                parent = current 
                current = current.right 
        
        node = BST(value)
        parent.left = node if not parent.left else None 
        parent.right = node if not parent.right else None 



    def contains(self, value):
        # Write your code here.
        
        if self is None:
            return False 
        
        if self.value > value:
            return self.left.contains( value) if self.left else False
        elif self.value < value:
            return self.right.contains( value) if self.right else False
        else:
            return True 


    def remove(self, value):
        # Write your code here.
        # Do not edit the return statement of this method.
        return self
    


import unittest

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

        root.insert(12)
        self.assertTrue(root.right.left.left.value == 12)

        

        # root.remove(10)
        self.assertTrue(root.contains(10))
        self.assertFalse(root.contains(45))
        root.insert(45)
        self.assertTrue(root.right.right.right.value == 45)
        # self.assertTrue(root.value == 12)

        self.assertTrue(root.contains(15))

obj = TestProgram()
obj.test_case_1()