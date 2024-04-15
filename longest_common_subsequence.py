'''

Subsequence  : non consecutive 
'''


def longestCommonSubsequence(s1, s2):
    # tabulation approach 
    
    N = len(s1)
    M = len(s2)
    
    dp = [ [ 0 for _ in range(M+1)] for _ in range(N+1)]
    
    
    
    
    for i in range(1, N+1):
        for j in range(1, M+1):
            # index shifted, hence i-1 , j-1
            if s1[i-1] == s2[j-1]:
                dp[i][j] = 1 + dp[i-1][j-1]
                
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])
                
    # print("dp", dp)
    
    return dp[N][M]

def recursive_function(s1, s2):
    
    N = len(s1)
    M = len(s2)
    
    dp = [ [ -1 for _ in range(M+1)] for _ in range(N+1)]
    
    for i in range(N+1):
        dp[i][0] = 0 
    
    for j in range(M+1):
        dp[0][j] = 0
        
    def solve(idx1,idx2,dp):
        
        if idx1 < 0 or idx2 < 0:
            return 0
        
        if dp[idx1][idx2] != -1 :
            return dp[idx1][idx2]
        
        
        if s1[idx1-1] == s2[idx2-1]:
            dp[idx1][idx2] = 1 + solve(idx1-1, idx2-1, dp)
            
        else:
            dp[idx1][idx2] = max(solve(idx1-1, idx2,dp), solve(idx1, idx2-1,dp))
            
        
        return dp[idx1][idx2] 
    
    return solve(N,M,dp)

        
        
        


s1 = "abcduiab"

s2 = "abcab"

print(recursive_function(s1,s2))