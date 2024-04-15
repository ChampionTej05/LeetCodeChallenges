'''
https://leetcode.com/problems/count-nice-pairs-in-an-array/description/

Solution is modelled as per Two Sum Hashing solution 

a + rev(b) = b + rev(a) ==> a-rev(a) = b-rev(b)

1. for every element, calculate [a-rev(a)] and store it in map. 
    a. if the a-rev(a) exists in the map already, increase total count += mapper[a-rev(a)], and then mapper[a-rev(a)]+=1 
        this is done, because for j , total+=mapper[a-rev(a)] will consider all previous i that would have satisfied this condition 
    b. if not,store and set the value to 1 
2. Return total count
'''

class Solution(object):
    
    MOD = 10**9+7
    
    def reverse_integer(self, num):
        astr = str(num)
        astr = astr[::-1].lstrip('0')
        if astr == '':
            return 0
        aint = int(astr,10)
        return aint
        
    
    def countNicePairs(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        from collections import defaultdict
        mapper  = defaultdict(int)
        
        totalNicePairs = 0 
        
        for num in nums:
            curr = num - self.reverse_integer(num)
            if curr in mapper:
                totalNicePairs = (totalNicePairs+mapper[curr])%Solution.MOD
                mapper[curr] = (mapper[curr]+1)%Solution.MOD
            else:
                mapper[curr] =1 
                
        return totalNicePairs%Solution.MOD