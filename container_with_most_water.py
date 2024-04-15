'''
https://leetcode.com/problems/container-with-most-water/description/


2 pointer approach (Start with two ends, so that width is maximised )

I think a good explanation for why we move pointer with the lower height is because we already have the max area with that height - since it is the lower pointer that means that every other distance that is closer will always be a smaller distance with the same or less height which means smaller area. 
Therefore we do not need to look at every other combination with that pointer. 
ex: [1,8,6,2,5,4,8,3,7]
left at index = 0 -> 1 
right at index = 8 --> 7 
area = min(1,7)* (8-1) = 7 
now even if consider all other indexes from right, area can never be greater than existing one, provided we fix the left pointer 

On generalisation --> for any lower  pointer(than corresponding other ptr), the max area can be formed with extreme pointer only 
'''

class Solution(object):
    
    def BruteForce(self, height):
    
        maxArea = 0 
        N = len(height)
        for i in range(N):
            for j in range(i+1, N):
                rectWidth = abs(i-j)
                rectHeight = min(height[i], height[j])
                area = rectWidth*rectHeight 
                maxArea = max(maxArea, area)
        
        return maxArea
    
    def maxArea(self, height):
        N = len(height)
        maxArea = 0 
        
        left = 0 
        right = N-1 
        
        # need two different lines to form the container always 
        while left < right :
            currentArea = min(height[left], height[right]) * (right-left)
            maxArea = max(maxArea, currentArea)
            
            if height[left] < height[right]:
                left +=1 
            else:
                # for equal heights, it should not matter which ones we shift 
                right-=1
                
        return maxArea 
            
    
    # Incorrect Solution ex: [1,2,4,3] , ans = 3, expected =4 
    def maxAreaIncorrect(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        

        minCont = (height[0],0)
        maxCont = (height[0],0)
        N = len(height)
        ptr = 1 
        maxWaterArea = 0 

        while ptr < N:

            waterWithPreviousCont = min(height[ptr], height[ptr-1])*1 
            waterWithMinCont = min(minCont[0], height[ptr])* abs((minCont[1]-ptr))
            waterWithMaxCont = min(maxCont[0], height[ptr]) * abs((maxCont[1]-ptr))
            maxWaterArea = max(waterWithPreviousCont, waterWithMinCont, waterWithMaxCont, maxWaterArea)
            

            if height[ptr] < minCont[0]:
                minCont = (height[ptr], ptr)
            if height[ptr] > maxCont[0]:
                maxCont = (height[ptr], ptr)



            ptr+=1 

        return maxWaterArea