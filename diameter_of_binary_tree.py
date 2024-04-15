
#this bascially gives the height of the tree 
def node_depth(root):
    if root is None:
        depth = 0 
        diameter =0 
        return depth, diameter
    

    left_depth , left_max_diameter = node_depth(root.left)
    right_depth , right_max_diameter = node_depth(root.right)

    # this would be diameter of the current node 
    local_diamter = left_depth  + right_depth 

    # maximum we have found this time
    max_diameter = max(left_max_diameter, right_max_diameter, local_diamter)

    # return subtree's height 
    return max(left_depth, right_depth) + 1 , max_diameter








    

