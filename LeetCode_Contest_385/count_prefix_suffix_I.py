'''
https://leetcode.com/contest/weekly-contest-385/problems/count-prefix-and-suffix-pairs-i/

'''

class Solution(object):
    def countPrefixSuffixPairs(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        
        count = 0 
        
        if len(words) < 2:
            return 0 
        

        for i in range(len(words)-1):
            for j in range(i+1, len(words)):
                if words[j].startswith(words[i]) and words[j][::-1].startswith(words[i][::-1]):
                    count+=1 
                    
                    
        return count
                    
                    
words = ["a","aba","ababa","aa"]
# words = ["pa","papa","ma","mama"]
words = ["abab","ab"]

obj = Solution()

print(obj.countPrefixSuffixPairs(words))