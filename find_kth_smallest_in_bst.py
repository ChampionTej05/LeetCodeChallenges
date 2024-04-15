'''
https://leetcode.com/problems/kth-smallest-element-in-a-bst/

We can use inOrder and restrict it to the Kth count 
'''
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class TreeNodeInfo:
    def __init__(self, nodesVisited = 0, currentVisitedNode = None):
        self.nodesVisited = nodesVisited
        self.currentVisitedNode = currentVisitedNode

def inOrderTraversal(root, k, treeInfo:TreeNodeInfo):
    if root is None or treeInfo.nodesVisited >=k:
        return 


    inOrderTraversal(root.left, k, treeInfo)

    if treeInfo.nodesVisited <k:
        treeInfo.nodesVisited +=1
        treeInfo.currentVisitedNode = root 
        inOrderTraversal(root.right, k, treeInfo)


     




## This is augmented BST approach, if multiple insert and delete operations are done on tree and kth smallest is required 
        
class AugmentedBST:
    def __init__(self):
        self.root = None

    def insert(self, val):
        self.root = self._insert(self.root, val)

    def _insert(self, node, val):
        if not node:
            return TreeNode(val)

        if val < node.val:
            node.left = self._insert(node.left, val)
        else:
            node.right = self._insert(node.right, val)

        node.subtree_size = 1 + self._get_size(node.left) + self._get_size(node.right)
        return node

    def delete(self, val):
        self.root = self._delete(self.root, val)

    def _delete(self, node, val):
        if not node:
            return node

        if val < node.val:
            node.left = self._delete(node.left, val)
        elif val > node.val:
            node.right = self._delete(node.right, val)
        else:
            # Node with only one child or no child
            if not node.left:
                return node.right
            elif not node.right:
                return node.left

            # Node with two children: Get the inorder successor
            temp = self._min_value_node(node.right)
            node.val = temp.val
            node.right = self._delete(node.right, temp.val)

        node.subtree_size = 1 + self._get_size(node.left) + self._get_size(node.right)
        return node

    def _min_value_node(self, node):
        current = node
        while current.left:
            current = current.left
        return current

    def _get_size(self, node):
        return node.subtree_size if node else 0

    def kth_smallest(self, k):
        return self._kth_smallest(self.root, k)

    def _kth_smallest(self, node, k):
        if not node:
            return None

        left_size = self._get_size(node.left)

        if k == left_size + 1:
            return node.val
        elif k <= left_size:
            return self._kth_smallest(node.left, k)
        else:
            return self._kth_smallest(node.right, k - left_size - 1)
