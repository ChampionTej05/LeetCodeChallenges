def helper(root, depth=0):
    if root:
        # 
        return depth + helper(root.left, depth+1) + helper(root.right, depth+1)
    else:
        return 0
        


def nodeDepths(root):
    # Write your code here.
    current_depth =0 
    return helper(root, current_depth)


    

# This is the class of the input binary tree.
class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
