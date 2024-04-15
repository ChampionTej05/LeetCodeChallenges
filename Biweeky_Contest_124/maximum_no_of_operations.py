'''
https://leetcode.com/contest/biweekly-contest-124/problems/maximum-number-of-operations-with-the-same-score-i/

'''

class Solution(object):
    def maxOperations(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        #brute force 
        
        count  =0 
        
        index = 0 
        elements_sum = nums[1]+nums[0]
        
        while index < len(nums)-1:
            print("index: {}, sum: {}".format(index, nums[index]+nums[index+1] ))
            if nums[index]+nums[index+1] == elements_sum:
                count+=1
            else:
                return count
            index = index + 2
            
        return count
    
    
nums = [3,2,1,4,4,1,3,2] 

obj = Solution()
print(obj.maxOperations(nums))
    
     