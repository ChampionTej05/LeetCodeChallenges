'''
https://leetcode.com/problems/largest-divisible-subset/description/?envType=daily-question&envId=2024-02-08

ex: [1,2,3]
valid pairs for this with (i,j)or (j,i)
(1,2) <-> (2,1)  => 2%1 =0
(1,3) <->(3,1)   => 3%1 =0
(2,3) <-> (3,2) => none of the i, j satisfy the condition 

1. Use BFS to generate subsets of the given set (as we want largest size answer, so level wise traversal is best)
2. Use DP matrix to store the answer for each (i,j) 
3. For each subset, generate pairs and find out answer 
'''


UNKNOWN = -1 
PRESENT = 1 
ABSENT = 0 



class Solution(object):

    def is_valid_divisible_subset(self, subset):
        for i in range(len(subset)-1):
            for j in range(i+1, len(subset)):
                if subset[i]%subset[j] !=0 and subset[j] % subset[i] != 0:
                    return False 
                
        return True 

    # Brute Force O(2**N) * (N*N) where N = len(nums)
    def generate_subsets(self, start_index, nums, current_subset, largest_subset):
        
        if start_index == len(nums) :
            if self.is_valid_divisible_subset(current_subset) and  len(current_subset) > len(largest_subset[0]):
                #update current subset 
                largest_subset[0] = current_subset[:] # copy or deep copy
            return 
        
        #include element current 
        current_subset.append(nums[start_index])
        self.generate_subsets(start_index+1, nums,  current_subset, largest_subset)

        #exclude element current 
        current_subset.pop()
        self.generate_subsets(start_index+1, nums,  current_subset, largest_subset)


    def largestDivisibleSubset(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        # count = self.recursive_computation(start_index=0, nums = nums, previous_element_index=-1, largest_subset=largest_subset)
        # print("largest subset", largest_subset)
        # print(count)
        # return count

        subset = self.largestDivisibleSubsetV1(nums)
        print(subset)
        return subset

    def largestDivisibleSubsetV1(self, nums):
            # Sort the nums list to ensure that every element can only be divided by its predecessors.
        nums.sort()
        # Memoization cache to store the largest subset ending at each index.
        memo = {}
        
        def dfs(prev_index, current_index):
            if current_index in memo:
                return memo[current_index]
            
            subset = []
            # From the current index, look forward to find elements divisible by the current element.
            for next_index in range(current_index + 1, len(nums)):
                if nums[next_index] % nums[current_index] == 0:
                    # Recursive call to find the largest subset from the next index.
                    next_subset = dfs(current_index, next_index)
                    if len(next_subset) > len(subset):
                        subset = next_subset
            
            # Include the current element in the subset.
            memo[current_index] = [nums[current_index]] + subset
            return memo[current_index]
        
        # Start the recursive search from a virtual index that "divides" all elements.
        # This avoids missing the first element in the nums list.
        largestSubset = []
        for i in range(len(nums)):
            subset = dfs(-1, i)
            if len(subset) > len(largestSubset):
                largestSubset = subset
        
        return largestSubset

    
    

nums = [1,4,7,2,16]
obj = Solution()
print(obj.largestDivisibleSubset(nums))