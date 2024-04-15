'''
https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/description/

Idea : We seatch for P and Q in subtrees. Any subtree which has P and Q both under it, will be answer for that level 
ex: for current node, if either of P and Q are under left and right subtree then it is the answer. 
If only one of them is found in either part, then that is the answer 

ChatGPT
The algorithm to find the LCA in a binary tree can be implemented using recursion. The idea is to traverse the tree starting from the root.
 For each node, we check if the current node is one of the two nodes for which we want to find the LCA. If it is, we return this node.
   Otherwise, we recursively search for the nodes in the left and right subtrees. The LCA will be the node where both recursive searches return a non-null result.
'''


def lowest_common_ancestor_binary_tree(root, p, q):

    if root is None:
        #very important, to decide when to end the search 
        return None 
    
    # matches the expected element in the search 
    if root==p or root==q:
        return root 
    
    left = lowest_common_ancestor_binary_tree(root.left, p, q)
    right = lowest_common_ancestor_binary_tree(root.right, p, q)

    if left and right:
        # i.e p or q are present in different branches of subtree, so root is answer
        return root 
    
    #else ancestor is the one of p and q 
    return  left if left else right
