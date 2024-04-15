'''
https://leetcode.com/contest/weekly-contest-381/problems/minimum-number-of-pushes-to-type-word-i/
'''
class Solution:
    def sumOfN(self,n:int) ->int:
        return (n*(n+1))//2
    def minimumPushes(self, word:str) -> int:
        N = len(word)
        quotient = N//8
        if quotient <=0:
            return N 

        print("N : {}, Quotient : {}".format(N, quotient))
        remainder = N%8 
        print("Remainder : {}".format(remainder))
        if remainder == 0 :
            return 8*self.sumOfN(quotient)
        
        

        ans = self.sumOfN(quotient)*8 + remainder *(quotient + 1) 
        return ans
        



word = "xycdefghijab"
obj = Solution()
print(obj.minimumPushes(word))