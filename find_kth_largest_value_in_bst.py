class BST:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def inOrderTraversal(tree, nodes):
    if tree is None:
        return
    inOrderTraversal(tree.left, nodes)
    nodes.append(tree.value)
    inOrderTraversal(tree.right, nodes)
    

def findKthLargestValueInBst(tree, k):
    # Write your code here.
    
    nodes = []
    inOrderTraversal(tree, nodes)
    print("Inorder traversal {}".format(nodes))

    print("Kth largest value in BST: {}".format(nodes[-k]))

    return nodes[-k]


def findKthLargestValueInBst_v1(tree, k):
    # Write your code here.
    nodes = inOrderTraversalReverse(tree, [], k)
    print("ans ", nodes)
    return nodes[-1]
    # return -1

    # avg: O(h+k) time and O(k) space 
    #  worst : O(n) time and O(k) space if tree is completely on the right side 
def inOrderTraversalReverse(tree, nodes, k):
    if tree is None or len(nodes) >= k:
        return nodes
    nodes = inOrderTraversalReverse(tree.right, nodes, k)
    if len(nodes) == k:
        print("returning with K elements", nodes)
        return nodes
    nodes.append(tree.value)
    nodes = inOrderTraversalReverse(tree.left, nodes, k)
    return nodes



def TreeInfo():

    def __init__(self):
        self.nodesVisitedTillNow = 0 
        self.lastVisitedNode = None 


def reverseTraverse(tree, treeInfo, k):

    if tree is None or treeInfo.nodesVisitedTillNow >= k:
        return 

    reverseTraverse(tree.right, treeInfo, k)

    #go in the left subtree, only if we haven't found our answer 
    if treeInfo.nodesVisitedTillNow < k:
        treeInfo.lastVisitedNode = tree 
        treeInfo.nodesVisitedTillNow +=1 
        reverseTraverse(tree.left, treeInfo, k)




