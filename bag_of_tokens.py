'''
https://leetcode.com/problems/bag-of-tokens/?envType=daily-question&envId=2024-03-02

Intuition:
1. We can increase score only by using lower tokens than power 
2. To get lower tokens than power, power should be maximised 
3. We will try to get at least one score first which is just less than power 
4. With this score, get maximum token available to increase the power 
5. With this increased power, increase score using lower tokens 
6. Once the tokens[start]>power, repeat 4 to 5 
'''


class Solution(object):
    def bagOfTokensScore(self, tokens, power):
        """
        :type tokens: List[int]
        :type power: int
        :rtype: int
        """
        
        tokens.sort()
        N = len(tokens)
        visited = [False]*N 
        tokens_checked = 0 
        
        maxScore = 0 
        start = 0 
        end = N-1 
        localScore = 0
        
        while tokens_checked < N:
            
            if tokens[start] <= power and not visited[start]:
                power = power - tokens[start]
                visited[start]=True 
                localScore+=1
                maxScore = max(maxScore, localScore)
                start +=1
                
            else:
                if localScore >=1 and not visited[end]:
                    visited[end] = True 
                    power = power + tokens[end]
                    end -=1 
                    maxScore = max(maxScore, localScore)
                    localScore-=1 
            tokens_checked+=1 
            
        
        return maxScore
    


tokens, power = [400,100,200,300], 200

tokens, power = [200,100], 150

tokens, power = [100], 50

tokens, power = [600, 100,100, 200, 300, 500, 50, 50, 50], 50


obj = Solution()

print(obj.bagOfTokensScore(tokens, power))
                    
                