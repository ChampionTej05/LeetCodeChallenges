'''
https://leetcode.com/problems/all-elements-in-two-binary-search-trees/

2 Steps 
1. Inorder of the trees 
2. Merge function of the merge sort 
'''

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    
    def inOrder(self, root, ans):
        if root == None:
            return 
        
        self.inOrder(root.left, ans)
        ans.append(root.val)
        self.inOrder(root.right, ans)
        
    def merge_two_sorted_lists(self, arr1, arr2):
        N = len(arr1)
        M = len(arr2)
        
        K = min(N, M)
        ptr1 = 0
        ptr2 = 0 
        tempArr = []
        while ptr1<N and ptr2<M:
            if arr1[ptr1] <= arr2[ptr2]:
                tempArr.append(arr1[ptr1])
                ptr1+=1 
            else:
                tempArr.append(arr2[ptr2])
                ptr2+=1 
                
                
        while ptr1<N:
            tempArr.append(arr1[ptr1])
            ptr1+=1 
            
        while ptr2<M:
            tempArr.append(arr2[ptr2])
            ptr2+=1 
            
        return tempArr 
        
        

    def getAllElements(self, root1, root2):
        """
        :type root1: TreeNode
        :type root2: TreeNode
        :rtype: List[int]
        """
        arr1 = []
        self.inOrder(root1, ans=arr1)
        
        arr2 = []
        self.inOrder(root2, arr2)
        
        tempArr = self.merge_two_sorted_lists(arr1, arr2)
        return tempArr
        