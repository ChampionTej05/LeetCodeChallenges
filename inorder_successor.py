'''
https://www.algoexpert.io/questions/find-successor

Concepts

INORDER -> Left, Root , Right 
1. If found node has right child, then the successor would be the leftmost node in it's right subtree 
2. If found node has NO right child, then we need to use parents to find out the answer.
    a. Go up the parent for that node, till we found a parent node for which NODE is on left side 
    meaning, we need to find a first node for which our subtree (which contains the node) lies on its left 
    b. If we reach root in this process and still don't get answer, return NULL (because that would rightmost child of the tree) ex: 10

    5
   / \
  3   8
 / \   \
2   4   10


Here, if we need to find successor(4), since it has no right child, we go up the parent, and find first node for which subtree with 4 lies on LEFT side 
which is 1 


Here for 10, we go up to the root to find answer, but no node found for which subtree is in left, so return NULL 

'''



def findSuccessor(tree, node):

    # if none, then return 
    if tree is None:
        return 
    
    if tree == node:
        # node has right child ? 
        if node.right :
            return leftMostChild(node.right)
        else:
            # find the parent which has this node subtree on the left 
            
            # go up, till node is on the right  side
            while node.parent and node.parent.right == node:
                node = node.parent

            #explicit case of root need not be handled, as root.parent = NULL 
                
            return node.parent
    else:
        # find node 
        left = findSuccessor(tree.left, node)
        if left:
            return left 
        right = findSuccessor(tree.right, node)
        return right
    
#  no need of the tree traversal as node is directly given 
def findSuccessor(node):
    if not node:
        return None

    # If the node has a right child, return the leftmost child of the right subtree
    if node.right:
        return leftMostChild(node.right)

    # If the node has no right child, move up the ancestors
    # until we find a node that is the left child of its parent
    while node.parent and node.parent.right == node:
        node = node.parent

    return node.parent



def leftMostChild(tree):

    if tree is None:
        return None 
    
    while tree.left :
        tree = tree.left 

    return tree