class Solution(object):
    def countAlternatingSubarrays(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        
        total_subarrays = len(nums) 
        current_length = 0 

        for i in range(1, len(nums)):
            if nums[i] != nums[i - 1]:
                current_length += 1
            else:
                current_length = 0
            total_subarrays += current_length

        return total_subarrays
    
obj = Solution()

nums = [0,1,1,1]
nums = [1,0,1,0]
nums = [0,1,0,0,1,0]
nums = [0,1,0]
print(obj.countAlternatingSubarrays(nums))