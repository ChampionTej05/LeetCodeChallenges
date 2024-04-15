'''
https://leetcode.com/problems/sum-root-to-leaf-numbers/?envType=daily-question&envId=2024-04-15

1. Try creating numbers and then summing them once the number is formed 
2. max range of the number could be 10, so TC = 10 [To convert string into number] * 1000 [Maximum Nodes in the tree] * 10 [Max depth] = 10**5 

So Brute force should work here

Function(root, current_number, numbers_formed)



'''

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    
    def traversal(self, root, current_number, numbers):
        if root is None:
            return 
        
        current_number.append(str(root.val))
        if not root.left and not root.right:
            numbers.append(int("".join(current_number)))
            
        if root.left:
            self.traversal(root.left, current_number, numbers)
            current_number.pop()
        if root.right:
            self.traversal(root.right, current_number, numbers)
            current_number.pop()
        
        
    def optimised(self, root, number, answer):
        if root is None:
            return 
        
        # every number will be multiplied by the 10 at each level because of this expression 
        # ex: 4-->9-->1 : 
        # at level0: number = 0*10+4 = 4 
        # at level1: number = 4*10+9 = 49 
        # at level2: number = 49*10+1=491 
        number = number * 10 + root.val 
        
        if not root.left and not root.right:
            answer.append(number)
            
        self.optimised(root.left, number, answer)
        self.optimised(root.right, number, answer)
    
    def sumNumbers(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        
        numbers = []
        current_number = []
        self.traversal(root, current_number, numbers)
        print("Numbers: ", numbers)
        print("current number", current_number)
        return sum(numbers)
        