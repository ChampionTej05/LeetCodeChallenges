'''
https://leetcode.com/problems/maximize-consecutive-elements-in-an-array-after-modification/


After sorting, at every element we have 2 choices (order is important )
        - consider ele+1 
        - consider ele 

        dp[ele]: maximum consecutive length possible till element = ele 

        case1: dp[ele+1] = dp[ele] + 1
        case2: dp[ele] = dp[ele-1] + 1 

        base : dp[0]=0 #no elements are smaller than 1
        
    
        
        for i in range(sorted(array)):
            dp[array[i]+1] = dp[array[i]] + 1 
            dp[array[i]] = dp[array-1] + 1 
            
        return max(dp.values())
        
'''

class Solution(object):
    def maxSelectedElements(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        '''
         

        
        '''
        
        mapper = {}
        mapper[0] = 0 
        nums.sort()
        
        for ele in nums:
            mapper[ele+1]  = mapper.get(ele, 0) + 1
            mapper[ele] = mapper.get(ele-1 , 0) + 1
            
            
        return max(mapper.values())