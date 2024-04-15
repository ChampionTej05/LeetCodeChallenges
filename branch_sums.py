'''
Find branch sum of binary tree 
'''

# This is the class of the input root. Do not edit it.
class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def branchSums(root, branch_sum=0, result=[]):
    # Write your code here.
    
    if root is None:
        return result
    branch_sum += root.value

    if root.left is None and root.right is None:
        #leaf node 
        result.append(branch_sum)
        return 
    
    if root.left :
        branchSums(root.left, branch_sum, result)
    if root.right:
        branchSums(root.right,branch_sum, result)

        

