'''

https://leetcode.com/problems/maximum-difference-between-node-and-ancestor/description/?envType=daily-question&envId=2024-01-11


Here is how approach would be 

if not root:
    return 0 
maxDiff = max(maxDiff, abs(root.val-maxAncestor), abs(root.val-minAncestor))
maxAncestor = max(maxAncestor, root)
minAncestor = min(minAncestor, root)
leftMaxValue = DFS(root.left, maxAncestor, minAncestor, maxdiff)
rightMaxValue = ... 
return max(leftMaxValue, rightMaxValue)
'''


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def maxAncestorDiff(self, root: [TreeNode]) -> int:
        def DFS(root, maxAncestor, minAncestor,maxDiff):

            if not root:
                # nothing here , return maxDiff found till now 
                return maxDiff 
            
            maxDiff = max(maxDiff , abs(root.val-minAncestor), abs(root.val-maxAncestor))

            #update ancestor for subtrees 

            maxAncestor = max(maxAncestor, root.val)
            minAncestor = min(minAncestor, root.val)

            left_max_diff  = DFS(root.left, maxAncestor, minAncestor, maxDiff)
            right_max_diff = DFS(root.right, maxAncestor, minAncestor, maxDiff)

            return max(maxDiff, left_max_diff, right_max_diff)
        
        return DFS(root, root.val, root.val,0)
    

'''
Iterative solution 

class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0 

        stk = [(root, -1, 1e6)] 
        ans = 0 

        while stk:
            node, maxSoFar, minSoFar = stk.pop() 
            maxSoFar = max(maxSoFar, node.val)
            minSoFar = min(minSoFar, node.val) 
            ans = max(ans, maxSoFar - minSoFar) 
            if node.left:
                stk.append((node.left, maxSoFar, minSoFar))
            if node.right:
                stk.append((node.right, maxSoFar, minSoFar))  
        
        return ans
'''