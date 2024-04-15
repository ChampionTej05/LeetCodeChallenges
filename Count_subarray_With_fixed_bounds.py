'''

https://leetcode.com/problems/count-subarrays-with-fixed-bounds/

https://www.youtube.com/watch?v=7l_GQIUGFQU
'''

class Solution(object):
    def countSubarrays(self, nums, minK, maxK):
        """
        :type nums: List[int]
        :type minK: int
        :type maxK: int
        :rtype: int
        """
        
        
        
        minKIndex, maxKIndex = -1, -1 
        N = len(nums)
        leftBoundary = -1 
        subArrayCount = 0 
        
        
        for current in range(N):
            
            # check if the current element is boundary element(s)
            if (nums[current] == minK):
                minKIndex = current
                
            if (nums[current] == maxK):
                maxKIndex = current 
                
            # if none of them, then we need to check if this is out of bound element, partioning array 
            
            if (nums[current] < minK or nums[current] > maxK):
                leftBoundary = current
                
            # if we have found valid subarray yet (all indexes not set to -1), then check if the answer can be calculated 
            
            if (minKIndex!=-1 and maxKIndex!=-1):
                smallerIndexOfBoundaryElement = min(minKIndex, maxKIndex)
                # if this condition is negative, that means, there exists leftBoundary(out of bound element), which is further away than possible boundary element 
                # ex: [1,2,5,7] LB = 7, minK=1, maxK=5 
                if (smallerIndexOfBoundaryElement - leftBoundary>0):
                    subArrayCount += smallerIndexOfBoundaryElement - leftBoundary
                    
        return subArrayCount
        
        
nums, minK, maxK = [1,3,5,2,7,5], 1,5

obj = Solution()

print(obj.countSubarrays(nums, minK, maxK ))