'''
https://leetcode.com/problems/furthest-building-you-can-reach/?envType=daily-question&envId=2024-02-08


Using Min heap 
- Store the depth of the consecutive building in the min heap 
- once the heap size crosses ladders, start using bricks for the buildings with minimum difference 

'''

class Solution(object):
    def furthestBuilding(self, heights, bricks, ladders):
        """
        :type heights: List[int]
        :type bricks: int
        :type ladders: int
        :rtype: int
        """
        
        
        from heapq import heapify, heappush, heappop
        
        # min-heap 
        building_heap = []
        heapify(building_heap)
        
        for i in range(1, len(heights)):
            depth_difference = heights[i] - heights[i-1]
            if depth_difference > 0:
                heappush(building_heap, depth_difference)
                
                # if this has caused that we are using more ladders than expected 
                if len(building_heap) > ladders:
                    
                    #start using bricks for the min-height if bricks exists 
                    building_depth = heappop(building_heap)
                    if bricks - building_depth >= 0:
                        bricks = bricks - building_depth
                    else:
                        return i-1
                    
        return len(heights)-1
                        
                        
heights = [14,3,19,3]
bricks = 10
ladders = 1
obj = Solution()

print(obj.furthestBuilding(heights, bricks, ladders))