'''
https://leetcode.com/problems/balanced-binary-tree/

Logic:
Get subtree depth and find if they differ by more than one 
'''


def helper(root, current_depth):
    
    if root is None:
        return current_depth,True
    else:
        # we don't want to sum, so do not add the path for current node 
        left_depth, left_balanced = helper(root.left, current_depth+1)
        right_depth,right_balaced = helper(root.right, current_depth+1)

        node_depth = max(left_depth, right_depth)
        
        if abs(left_depth-right_depth) <=1 and left_balanced and right_balaced:
            return node_depth, True 
        else:
            return node_depth, False
