'''
https://leetcode.com/problems/custom-sort-string/?envType=daily-question&envId=2024-03-06

Create mapper from S2 , to map , which character from S2, occurs at how many indexes in S2 

For chr in S1, 
    - check if exists in S1 
    - if yes, append all instances of that character in S2, to arr
    - in no, skip 
    
for characters which are yet not mapped 
    - append them in any order 
'''

class Solution(object):
    def customSortString(self, order, s):
        """
        :type order: str
        :type s: str
        :rtype: str
        """
        from collections import defaultdict
        mapperS = defaultdict(int)
        
        for chr in s:
            mapperS[chr]+=1 
        
        print("mapper S", mapperS)
        
        resultS = []
        
        for chr in order:
            if chr in mapperS:
                tempS = str(chr)*mapperS[chr]
                mapperS[chr] = 0 
                resultS.extend(tempS)
                
        
        #for all unmapped characters in S , put them at the end 
        
        for chr, count in mapperS.items():
            if mapperS[chr] != 0 :
                tempS = str(chr)*mapperS[chr]
                resultS.extend(tempS)
                
        return ''.join(resultS)