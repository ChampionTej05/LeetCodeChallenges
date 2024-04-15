'''
https://takeuforward.org/data-structure/longest-common-substring-dp-27/

Substring: Consecutive Characters 
'''


def longestCommonSubstring(s1, s2):
    # tabulation approach 
    
    N = len(s1)
    M = len(s2)
    
    dp = [ [ 0 for _ in range(M+1)] for _ in range(N+1)]
    
    
    maxLen = 0
    
    for i in range(1, N+1):
        for j in range(1, M+1):
            # index shifted, hence i-1 , j-1
            if s1[i-1] == s2[j-1]:
                dp[i][j] = 1 + dp[i-1][j-1]
                maxLen = max(dp[i][j], maxLen)
            else:
                dp[i][j] = 0 
                
    print("dp", dp)
    
    return maxLen


s1 = "acd"
s2 = "abzscd"

print(longestCommonSubstring(s1, s2))