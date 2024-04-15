'''

https://leetcode.com/problems/minimize-manhattan-distances/

https://www.youtube.com/watch?v=0yRcwMrawN0

'''



class Solution(object):
    def minimumDistance(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        
        
        # we will first find the maximum manhatten distance in the array and points giving that answer 
        INT_MIN = -10**9
        INT_MAX = 10**9
        def maxMH(points, skip=None):
            
            maxSum = (-1, INT_MIN)
            minSum = (-1, INT_MAX)
            
            maxDiff = (-1, INT_MIN)
            minDiff = (-1, INT_MAX)
            
            for i in range(len(points)):
                # not calculating for this index 
                if i == skip : 
                    continue
                currentSum = points[i][0]+points[i][1]
                currentDiff = points[i][0]- points[i][1]
                
                if currentSum > maxSum[1]:
                    maxSum = (i, currentSum)
                if currentSum < minSum[1]:
                    minSum = (i, currentSum)
        
                if currentDiff > maxDiff[1]:
                    maxDiff = (i, currentDiff)
                if currentDiff < minDiff[1]:
                    minDiff = (i, currentDiff)
                    
            print("Sum : ", maxSum, minSum)
            print("Diff: ", maxDiff, minDiff)
            
            if maxSum[1]-minSum[1] > maxDiff[1]-minDiff[1]:
                return (maxSum[1]-minSum[1], maxSum[0], minSum[0])
            else:
                return (maxDiff[1]-minDiff[1], maxDiff[0], minDiff[0])
            
        
        _, P_i, P_j = maxMH(points)
        
        # remove P_i and calculate MH 
        maxMHDistance_without_P_i, _ , _ = maxMH(points, skip = P_i)
        maxMHDistance_without_P_j, _ , _ = maxMH(points, skip= P_j)
        print("without P_i", maxMHDistance_without_P_i)
        print("without P_j", maxMHDistance_without_P_j)
        return min(maxMHDistance_without_P_j, maxMHDistance_without_P_i)
        


obj = Solution()

points = [[3,10],[5,15],[10,2],[4,4]]

print(obj.minimumDistance(points))