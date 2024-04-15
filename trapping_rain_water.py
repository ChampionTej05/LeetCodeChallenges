'''
https://leetcode.com/problems/trapping-rain-water/?envType=daily-question&envId=2024-04-11

Approach 
Using O(N*N) solution

WaterTrapped[i] = MIN(leftBoundary[i], rightBoundary[i]) - elevation[i]

leftBoundary[i] = max(elevation[j]) where j=i to j=0
rightBoundary[i]= max(elevation[j]) where j=i to j=N-1


Optimisation: Can we optimise the inner loop where we are calculating the left and right boundaries repetedly 
- We do the left and right boundary computation for each I, where we are repetedly calculating left side max and right side max 
- This we can precompute like prefix array during (product of all except self kind of questions)

Precompute leftBoundary -> max(leftMax, height[i]) 
Use that for trapping calculation 
'''

class Solution(object):

    def trapWaterBruteForce(self, height):
        
        totalWaterTrapped = 0 
        N = len(height)
        for i in range(N):
            
            maxLeftBoundaryI = 0 
            maxRightBoundaryI = 0
            
            # calculate max from j=i to j=0
            maxLeftBoundaryI = max(height[:i+1])
            maxRightBoundaryI = max(height[i:])
            
            # print("Max Left %s at i %s".format( maxLeftBoundaryI, i))
            # print("Max right: %s at i :%s".format(maxRightBoundaryI, i))
            
            waterTrappedI = min(maxRightBoundaryI, maxLeftBoundaryI)-height[i]
            # print("Water trapped: %s at i :%s".format(waterTrappedI, i))
            
            totalWaterTrapped+=waterTrappedI
        
        
        return totalWaterTrapped
    
    def getLeftBoundaries(self, height):
        N = len(height)
        leftBoundaries = []
        leftMax = 0 
        
        for i in range(N):
            leftMax = max(leftMax, height[i])
            leftBoundaries.append(leftMax)
            
        return leftBoundaries
    
    def getRightBoundaries(self, height):
        N = len(height)
        rightBoundaries = []
        rightMax = 0 
        
        for i in reversed(range(N)):
            rightMax = max(rightMax, height[i])
            rightBoundaries.append(rightMax)
            
        return rightBoundaries[::-1]
        
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        
        # return self.trapWaterBruteForce(height)
        totalWaterTrapped = 0 
        
        N = len(height)
        leftBoundaries = self.getLeftBoundaries(height)
        rightBoundaries = self.getRightBoundaries(height)
        
        print("Left Boundary", leftBoundaries)
        print("Right Boundary", rightBoundaries)
        
        for i in  range(N):
            waterTrappedI = min(leftBoundaries[i], rightBoundaries[i]) - height[i]
            print("Water trapped: {} at i :{}".format(waterTrappedI, i))
            
            totalWaterTrapped+= waterTrappedI
            
        return totalWaterTrapped
    
    
obj = Solution()

height = [0,1,0,2,1,0,1,3,2,1,2,1]

assert obj.trap(height) == 6

height = [4,2,0,3,2,5]
assert obj.trap(height) == 9
    
    
            