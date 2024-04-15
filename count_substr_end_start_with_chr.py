'''
https://leetcode.com/contest/weekly-contest-389/problems/count-substrings-starting-and-ending-with-given-character/

'''

class Solution(object):
    def countSubstrings(self, s, c):
        """
        :type s: str
        :type c: str
        :rtype: int
        """
        
        count = 0 
        N = len(s)
        
        left = None
        
        right = 0 
        
        while right < N:
            
            if s[right] == c and left == None:
                # first match 
                left = right 
                count +=1 
            else:
                count+=1 
                

            right+=1 
            
            
        if left == None: 
            return -1 
        if count == 1:
            return 1
        
        return count*(count-1)