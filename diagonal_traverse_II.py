'''
https://leetcode.com/problems/diagonal-traverse-ii/

HINT: Create map of sum of indexes. Store cells for each of that map 

map[0+0]
map[0+1]
map[1+1]
'''

class Solution(object):
    def findDiagonalOrder(self, nums):
        """
        :type nums: List[List[int]]
        :rtype: List[int]
        """
        
        from collections import defaultdict
        
        mapper = defaultdict(list)
        
        for i in range(len(nums)):
            for j in range(len(nums[i])):
                mapper[i+j].append(nums[i][j])
                
        print(mapper)
        
        answer = []
        
        for k, v in mapper.items():
            answer.extend(v[::-1])
            
        return answer 
        
        
