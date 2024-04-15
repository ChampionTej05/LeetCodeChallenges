'''
https://leetcode.com/problems/isomorphic-strings/?envType=daily-question&envId=2024-04-02

If the letter a-->e is mapped like this, then a could never be mapped to anyone else and same goes for e
What we can do is:
1. Create two maps. 
2. For s[i], map[s[i]] = i and map[t[i]] = i 
3. Next time check if map[s[i]] exists and is it equal to value of map[t[i]]
4. If not, return false
'''

class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        from collections import defaultdict
        sMap, tMap = {}, {}
        
        if len(s)!=len(t):
            return False 
        
        for i in range(len(s)):
            
            if sMap.get(s[i],0) != tMap.get(t[i],0):
                return False 
            
            if sMap.get(s[i],0) == 0:
                sMap[s[i]] = i +1
            if tMap.get(t[i],0) == 0:
                tMap[t[i]] = i+1
            
            print(sMap, tMap)
            
        return True 
    
    def fastSolution(s,t):
        return len(set(s)) == len(set(zip(s,t))) == len(set(t))
    
    
obj = Solution()

s, t = "add", "bcc"
s, t = "paper", "title"
s, t = "bbbaaaba", "aaabbbba"
s, t= "badc", "baba"

print(obj.isIsomorphic(s,t))

        