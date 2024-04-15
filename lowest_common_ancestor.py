'''
https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/

1. find all ancestors of P and Q 
2. Find first mis-matching ancestor from Root 
OR
1. lowest common ancestor is the node on which we have to PART our ways during search of the node. 
so if p,q both lies on same side, we continue on that side else we return the current node 
'''

def find_ancestor(root, node):
    current = root 
    ancestors = []

    ancestors.append(current)
    while current != None:
        if current.val == node.val:
            break
        if node.val < current.val  :
            current = current.left 
        else:
            current = current.right 
        
        ancestors.append(current)

    
    return ancestors


def find_lowest_common_ancestor_helper(arrP, arrQ):
    smallest_array =  arrP if len(arrP)<len(arrQ) else arrQ
    i = 0 

    while i < len(smallest_array):
        if arrP[i] != arrQ[i]:
            # expected i is not 0 here, if it is, then no ancestor exists which can not be possible 
            return smallest_array[i-1]
        i+=1 

    return smallest_array[i-1]


def print_tree(arr):
    i = 0 
    while i <len(arr) and arr[i] :

        print(arr[i].val, end = " -> ")
        i+=1
    
    print(" ")

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """

        arrP = find_ancestor(root, p)
        arrQ = find_ancestor(root, q)

        print_tree(arrP)
        print_tree(arrQ)

        ancestor = find_lowest_common_ancestor_helper(arrP, arrQ)
        print(ancestor.val)
        return ancestor 
    
def optimised_lowest_common_ancestor(root, p , q):

    current = root 

    while current != None:
        if p.val < current.val and q.val < current.val:
            #go on left , as both are less 
            current = current.left 
        elif p.val > current.val and q.val > current.val:
            current = current.right 
        else:
            return current 

    #no return expecting that, p & q exists in the tree 


import unittest
# Helper function to build a BST from a list for testing
def insert_level_order(arr, root, i, n):
    if i < n:
        temp = TreeNode(arr[i])
        root = temp
        root.left = insert_level_order(arr, root.left, 2 * i + 1, n)
        root.right = insert_level_order(arr, root.right, 2 * i + 2, n)
    return root

class TestLowestCommonAncestor(unittest.TestCase):
    def test_lca(self):
        arr = [6, 2, 8, 0, 4, 7, 9, None, None, 3, 5]
        root = insert_level_order(arr, None, 0, len(arr))
        sol = Solution()
        
        # Test case 1
        p, q = TreeNode(2), TreeNode(8)
        self.assertEqual(sol.lowestCommonAncestor(root, p, q).val, 6)
        self.assertEqual(optimised_lowest_common_ancestor(root,p,q).val,6)

        # Test case 2
        p, q = TreeNode(2), TreeNode(4)
        self.assertEqual(sol.lowestCommonAncestor(root, p, q).val, 2)
        self.assertEqual(optimised_lowest_common_ancestor(root,p,q).val,2)




        # Add more test cases as needed



if __name__ == '__main__':
    unittest.main()