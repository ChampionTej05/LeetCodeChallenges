'''
https://leetcode.com/problems/perfect-squares/description/?envType=daily-question&envId=2024-02-08

Explore DFS or Recursion strategy similar to coin change
'''

class Solution:
    def __init__(self) -> None:
        self.memo = {}
    def DFS(self, start_number, target):
        if target in self.memo:
            return self.memo[target]
        
        if target == 0 :
            return 0 
        
        # invalid path , so we should return invalid answer, which would be infinity in this case 
        if target < 0 or start_number**2 > target:
            return float("inf")
        
        include_current_number = self.DFS(start_number, target-(start_number**2)) + 1 
        skip_current_number = self.DFS(start_number+1, target)


        self.memo[target] = min(include_current_number, skip_current_number)
        return self.memo[target]
    
    # one more way to do it, using loop 
    def minNumSquares(self, n: int) -> int:

        # Check if the result for n is already computed
        if n in self.memo:
            return self.memo[n]
        
        # Base cases
        if n == 0:
            return 0
        if n < 0:
            return float('inf')
        
        min_count = float('inf')
        i = 1
        while i**2 <= n:
            # Recursive call for the remaining value after subtracting a square
            current_count = 1 + self.minNumSquares(n - i**2)
            min_count = min(min_count, current_count)
            i += 1
        
        # Memoize the result before returning
        self.memo[n] = min_count
        return min_count
    
    def minNumSquaresUsingDP(self, n:int) -> int:
        dp = [float('inf') if i>2 else i for i in range(n+1)]
        import math 
        perfect_squares = [ i*i for i in range(1, int(math.sqrt(n))+1)]
        for target in range(2, n+1):
            for square in perfect_squares:
                if square <= target:
                    dp[target] = min(dp[target], dp[target-square]+1)
                else:
                    break
        
        return dp[n]
    
    def numSquares(self, n: int) -> int:
        
        # count = self.DFS(start_number=1, target=n)
        count = self.minNumSquaresUsingDP(n)
        print(count)
        return count
    


n = 4 

obj = Solution()

obj.numSquares(n)