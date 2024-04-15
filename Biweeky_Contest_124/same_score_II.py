'''
https://leetcode.com/contest/biweekly-contest-124/problems/maximum-number-of-operations-with-the-same-score-ii/

Recursion problem 

Base case : 
when Start, End go out of the Bounds or Expected Sum != sum(start+end) --> return score 

Computation:
Sum for all 3 paths 

Recursive:

Recurse for all 3 paths and get the score 

Return max score out of them all 

'''

class Solution(object):
    # won't work as it would be 3**N 
    # def evalulate(self, nums, start, end, expected_sum, score):
    #     N = len(nums)
    #     # base case 
        
    #     if start <0 or start >= N or end < 0 or end >= N:
    #         return score 
    
        
    #     current_path_sum = nums[start]+ nums[end]
        
    #     if current_path_sum == expected_sum:
    #         # first two elements : path1
    #         count1_path = self.evalulate(nums, start+2, end+2, expected_sum, score+1)
            
    #         # last two elements: path2
    #         count2_path = self.evalulate(nums, start-2, end-2, expected_sum, score+1)
            
    #         # first and last element : path3
    #         count3_path = self.evalulate(nums, start+1, end-1, expected_sum, score+1)
            
    #         return max(count1_path, count2_path, count3_path)
        
    #     else:
    #         return score 
        
    def init_memo(self, N):
        self.memo = [[-1 for _ in range(N)] for _ in range(N)]
        
    def evaluate_DP(self, nums, start, end, score):
        

        # base case, two elements should exists at least 
        N = len(nums)
        if start < 0 or start >= N or end < 0 or end >= N:
            return 0
        if end - start +1  < 2:
            return 0
        
        if start >=end  :
            return 0
        
        if self.memo[start][end] !=-1:
            return self.memo[start][end]

        max_score = 0  # Initialize max_score with the current score
        current_score = 0

        # Explore the three paths
        # Path 1: Remove the first two elements
        if  nums[start] + nums[start+1] == score:
            max_score = max(max_score, 1 +  self.evaluate_DP(nums, start + 2, end, score))

        # Path 2: Remove the last two elements
        if  nums[end] + nums[end-1] == score:
            max_score = max(max_score, 1 + self.evaluate_DP(nums, start, end - 2, score))

        # Path 3: Remove the first and last elements
        if nums[start] + nums[end] == score:
            max_score = max(max_score, 1 + self.evaluate_DP(nums, start + 1, end - 1, score))
        
        self.memo[start][end]= max_score  # Memoize the result
        return max_score
            
        
    
    def maxOperations(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        

        N = len(nums)
        if N < 2:
            return 0
        self.init_memo(N)
        path1 = self.evaluate_DP(nums, 0, N-1, nums[0]+nums[1])
        
        if path1 == N:
            return path1
        
        self.init_memo(N)
        path2 = self.evaluate_DP(nums, 0, N-1, nums[N-2]+ nums[N-1])
        
        if path2 == N:
            return path2
        self.init_memo(N)
        path3 = self.evaluate_DP(nums , 0, N-1, nums[0]+nums[N-1])
        
        return max(0, path1 , path2, path3)
        
        
        
nums = [3,2,1,2,3,4]
# nums = [3,2,6,1,4]
nums = [1,9,7,3,2,7,4,12,2,6]
nums = [1]*2000

obj = Solution()

print(obj.maxOperations(nums))