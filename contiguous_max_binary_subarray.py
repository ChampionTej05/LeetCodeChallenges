'''
https://leetcode.com/problems/contiguous-array/?envType=daily-question&envId=2024-03-13

NOTE: Main idea is using Hash Table to store relative count of 1 & 0 
SIMILAR : This question is similar to finding max subarray with sum=0
If we use count to increment everytime we see 1 and decrement when see 0 
Then Ideally, subarray having equal number of 1&0 will be in two cases 
    -> when count ==0 
    -> when count value is repeated which we have seen in past. Because if the count value is repeated 
        then values between that index and current index, will give equal count
[0,1,0,0,0,0,0,1,1,1,0,1]
[-1,0,-1,-2,-3,-4,-5,-4,-3,-2,-3,-2]

table[0] = -1 #sum 0 seen at index=-1 => start of the array 

count = 0, idx = 1 , ans = 1-0+1 =2

count = -4 idx = 7 , ans = 7-5 =2 [0,1] table[-4] = 7
count = -3 idx = 8 , ans = 8-4 = 4 [0,0,1,1] table[-3] = 8
count = -2 idx = 9 , ans = 9-3 = 6 [0,0,0,1,1,1] table[-2] = 9
count = -3 idx = 10, ans = 10-8= 2 [1,0] table[-3] = 10 
count = -2 idx = 11, ans = 11-9 = 2 [0,1] table[-2] = 11 

if count == 0 at last:
    return N 
    
ex: [1,0]
cnt: [1, 0]

count = 0 at last : --> return N 

ex: [0,1,1]



'''

class Solution(object):
    def findMaxLength(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        
        from collections import defaultdict
        maxLength = 0 
        N = len(nums)
        
        #  Brute Force Soluton 
        # for i in range(0, N):
        #     mapper = {0:0 , 1:0}
        #     for j in range(i, N):
        #         mapper[nums[j]]+=1 


        #     if mapper[0]==mapper[1]:
        #         maxLength = max(maxLength, j-i+1)

        countToIdxMapper = defaultdict(int)
        
        count = 0 # represent count of 1 & 0s 
        # in the start everything is 0 --> valid combinations 
        
        countToIdxMapper[0] = -1 # sum 0 seen at -1 index ==> before start of the array
        
        for idx, num in enumerate(nums):
            if num == 0:
                count-=1 
            else:
                count+=1 

            
            if count in countToIdxMapper:
                maxLength = max(maxLength, idx - countToIdxMapper[count])
            else:
                countToIdxMapper[count] = idx 
                
        
        if count == 0:
            return N 
        
        return maxLength
        
        