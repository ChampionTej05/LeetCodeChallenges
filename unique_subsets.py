

from typing import List




class Solution:
    
    #  this solution works if there are less paths to be explored 
    def subsetsWithDup_v1(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """

        subsets = set()
        N =  len(nums)

        #  generate all possible subsets first 
        def generate(index, current_subset):
            if index == N:
                # found all iterators possible 
                subsets.add(tuple(current_subset))
                return 


            #pick element and consider for current subset 
            current_subset.append(nums[index])
            generate(index+1, current_subset)


            #skip the element 
            current_subset.pop()
            generate(index+1, current_subset)

        nums.sort()
        generate(0, [])
        # print(subsets)
        answer = [ list(i) for i in subsets]
        return answer
    
    
    # better efficient solution 
    def subsetsWithDup(self, nums):
        
        subsets = set()
        
        N = len(nums)
        def generate(index, current_subset):
            
            #explored all paths 
            
            if index == N:
                subsets.add(tuple(current_subset))
                return 
            
            #include and explore this path 
            current_subset.append(nums[index])
            generate(index+1, current_subset)
            
            #exclude this element and keep on excluding all elements which are equal to this to reduce duplicate calls 
            current_subset.pop()
            
            i = index+1
            while i < N and nums[i] == nums[i-1]:
                i+=1
                continue 
            
            #we have reached the element which is not equal to nums[index] 
            #explore from this path again 
            generate(i, current_subset)
            
        nums.sort()
        generate(0, [])
        
        print(subsets)
        answer = [ list(i) for i in subsets]
        return answer
            
            
            
            
            
            
            

            
    
    
obj = Solution()
nums = [1,2,2]

print(obj.subsetsWithDup(nums))