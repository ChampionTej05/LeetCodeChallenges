'''
https://leetcode.com/problems/find-polygon-with-the-largest-perimeter/?envType=daily-question&envId=2024-02-08
'''

class Solution(object):
    def largestPerimeterBruteForce(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        '''
        1 , 1 , 2, 3, 5, 12, 50 
        prefix_sum 
        0, 1, 2, 4, 7, 12, 24, 74

        n1 = a[2] = 2
        n2 = a[0]+a[1] = 2 

        n2 = n1+n2 = 4
        n1 = 3  --> satisfied , total = 7

        n2 = n1+n2 = 7 
        n1 = 5 --> satisfied , total = 12 

        n2 = n1+n2 = 12 
        n2 = 12 --> not satisfied

        n2 = 12+12 = 24
        n1 = 50 --> not satisfied , total = 12 


        n2 : j = 2 to N 
        n1: i =0 to N-2 

    
        n1 = n[0] + n[1]

        n1 = n[1] + n[2]

        n1 = n[2] + n[3]
        n1 = n[i] + n[i+1]

        
        '''

        nums.sort()
        max_perimeter = 0 

        N = len(nums)
        for i in range(0, N-2):

            n2 = nums[i] + nums[i+1]
            for j in range(i+2, N):
                n1 = nums[j]
                if n2 > n1:
                    max_perimeter = max(max_perimeter, n1+n2)

                n2 = n1+n2 


        print(max_perimeter)
        return max_perimeter
    
    def largestPerimeter(self, nums):
        '''
        We don't need to calculate sub array.
        ex: 1, 1, 2, 3, 5, 12, 24 
        let us say 2+3+5 < 12 this satisfies the condition, so we might be tempted to return this 
        but since all elements are positive and sorted, even if we add elements before 2,3,5
        condition is gonna hold true 
        
        hence, just calculating running sum and checking if the next element is less than it , is sufficient  
        '''
        nums.sort()
        max_perimeter = -1 

        N = len(nums)
        current_sum = 0 

        for i in range(N):
            if nums[i] < current_sum:
                max_perimeter = current_sum+ nums[i]
            
            current_sum = current_sum+nums[i]

        


        print(max_perimeter)
        return max_perimeter
    