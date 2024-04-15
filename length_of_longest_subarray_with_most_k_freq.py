'''

https://leetcode.com/problems/length-of-longest-subarray-with-at-most-k-frequency/?envType=daily-question&envId=2024-03-25

Two Pointer 

1. We include any element in the window, if the freq[chr] < k before addition 
2. If not, then we need 
    a. update global maximum 
    b. Reduce count of all elements from start to index of chr in the array from the map 
    

'''

class Solution(object):
    def maxSubarrayLength(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        
        from collections import defaultdict
        mapper = defaultdict(int)
        
        start = 0 
        
        end =0 
        
        N = len(nums)
        globalMaxLength =0 
        localMaxLength =0
        while end < N:
            
            if mapper[nums[end]] < k:
                # increase count
                mapper[nums[end]]+=1 
                localMaxLength+=1
            else:
                # update the current max length  
                globalMaxLength = max(globalMaxLength, localMaxLength)
                
                
                # reduce count all elements from start to duplicate index 
            
                
                while start < end:
                    mapper[nums[start]]-=1
                    if nums[start] == nums[end]:
                        break
                    start+=1
                    
                # skipping the element which is equal to nums[end]
                start = start+1 
                
                localMaxLength =  end-start+1
                    
                # update the count with end 
                
                mapper[nums[end]]+=1 
                
            print("Mapper :{} at end :{}".format(mapper, end))
                
            end+=1 
                
        
        
        globalMaxLength = max(globalMaxLength, localMaxLength)
        
        return globalMaxLength
    
    


obj = Solution()


nums , k = [1,2,1,2,1,2,1,2] , 1

# nums ,k = [1,1,1,3], 2
print(obj.maxSubarrayLength(nums, k))