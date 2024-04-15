'''
https://leetcode.com/problems/validate-binary-search-tree/

Add bounds to each node during validation 

'''

def bst_validity_helper(root, minValue, maxValue):
    if root is None:
        return True 
    
    if root.val <= minValue or root.val >= maxValue:
        return False 
    
    left_validity = bst_validity_helper(root.left, minValue, root.val)
    if not left_validity:
        return False 
    
    right_validity = bst_validity_helper(root.right, root.val, maxValue)
    return right_validity and left_validity
    

