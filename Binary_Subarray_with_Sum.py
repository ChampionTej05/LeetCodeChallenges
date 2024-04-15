'''
https://leetcode.com/problems/binary-subarrays-with-sum/description/?envType=daily-question&envId=2024-03-13

for subarray , from idx=i to idx=j, 
PSum[j] - P[i-1] : will give the range sum between i->j 

Hence, we are looking for P[j]-P[i-1] = goal 
Hence, P[j]-goal = P[i-1]

So if we are standing at idx=j, then we need to find frequency of , P[j]-goal in past 
that, will be how many subarrays can be form, using J index 

NOTE : This solution works for non-binary array too
'''



class Solution(object):
    def numSubarraysWithSum(self, nums, goal):
        """
        :type nums: List[int]
        :type goal: int
        :rtype: int
        """
        from collections import defaultdict
        prefixSumFrequencyMapper = defaultdict(int)
        
        # since prefix sum = 0 always exists in array , for idx = -1 
        prefixSumFrequencyMapper[0] = 1
        
        prefixSum = 0 #storing prefix sum at index j 

        totalSubArrays = 0
        
        for j, num in enumerate(nums):
            
            prefixSum+= nums[j]
            
            # find how many times : prefixSum-goal exists in past 
            
            countOfPsumI = prefixSumFrequencyMapper[prefixSum-goal]
            
            totalSubArrays += countOfPsumI
            
            # Increase the frequency of this PSum 
            
            prefixSumFrequencyMapper[prefixSum]+=1 
            

        return totalSubArrays
    
    
    def TwoPointerSolution(self, nums, goal):
        '''
        Great solution with description by Aryan Mittal Youtube 
        
        When we are at index = j , we need to decide whether we should expand window or shrink window from back 
        
        If 0 , was not present, then we could have simply shrinked window whenever currentSum>goal 
        But now when currentSum==goal(due to including 0), we have two options 
         -> Shrink window always 
         -> Expand window always 
         
        ex:[1,0,1,0,0,0,1,1,0,0]
        '''