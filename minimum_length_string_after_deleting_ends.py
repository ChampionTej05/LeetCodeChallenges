'''
https://leetcode.com/problems/minimum-length-of-string-after-deleting-similar-ends/description/
'''

class Solution(object):    
    def minimumLength(self, s):
        """
        :type s: str
        :rtype: int
        """
        N = len(s)
        
        left = 0 
        right = N-1 
        
        if N<=1:
            return N 
        
        if  s[left]!=s[right]:
            return N 
            
        current_character = s[left]
        while (left < right):
            current_character = s[left]
            
            while (left <= right and s[left] == current_character):
                left +=1 
                
            while (left <= right and s[right] == current_character):
                right-=1
            
             
            print("Current character: ", current_character)
            print("left, right", left , right)

        return right-left+1
    
    
    def short_solution(self, s):
        left  = 0 
        N = len(s)
        right = N-1 
        while len(s) > 1 and s[0] == s[-1]:
            # remove all leading and ending characters which are same 
            s = s.strip(s[0])
        # if all characters are removed , then answer would be 0 
        #  if any of the charas is remaining, answer would be 1 or those many characters 
        return len(s)
            
            
            
        
        
                
            
            
            
s = "aabccabba" 
s = "aba"
s = "abba"
s = "ca"
s = "abbbbbbbaabbbbbbbaa"
# s = "aabbbbacba"
s = "abbbbba"
s = "abbbbbbbbbbbbbbbbbbba"

obj = Solution()
print(obj.minimumLength(s))
        