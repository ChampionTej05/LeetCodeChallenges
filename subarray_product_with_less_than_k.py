'''
https://leetcode.com/problems/subarray-product-less-than-k/description/?envType=daily-question&envId=2024-03-25

Two pointer approach 

1. Keep product variable to keep track of subarray product 
2. Keep on extending window on right and get the new product : product*=nums[right]
    1. If after extending window on right, product>=k, we reduce from left 
    2. Reduce from left and reduce product too , product/= nums[left]
3. After this, subarrays formed between left and right , will be our answer for current left and right 

4. Keep cumulative count 

subArrayInBetween = right - left + 1

ex: [5,2,3] 

if l=0 and r = 0 --> c = 1 (5)
l = 0, r = 1 --> c =2 (2, (2,5))
l =0, r = 2--> c= 3 (3, (2,3), (3,2,5)) 

so everytime c  = right-left+1 




'''


class Solution(object):
    def numSubarrayProductLessThanK(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        
        left = 0
        N = len(nums)
        
        product = 1 
        
        countOfSubArrays = 0 
        
        for right in range(N):
            product = product * nums[right]
            
            # reduce window if the product has overflown 
            
            while (left <= right and product >=k):
                product = product // nums[left]
                left +=1 
                
            
            subArrayInBetween = right - left + 1 
            
            countOfSubArrays += subArrayInBetween
            
        return countOfSubArrays