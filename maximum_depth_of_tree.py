'''
Maximum depth = Length of branch from Root node to it's farthest child 
'''



def helper(root, current_depth):
    
    if root is None:
        return current_depth
    else:
        # we don't want to sum, so do not add the path for current node 
        return  max(helper(root.left, current_depth +1), helper(root.right, current_depth+1) )
    

def maxNodeDepth(root):
    # Write your code here.
    current_depth =0 
    return helper(root, current_depth)



