class Solution(object):
    def maxBottlesDrunk(self, numBottles, numExchange):
        """
        :type numBottles: int
        :type numExchange: int
        :rtype: int
        """
        
        drunk = 0 
        empty = 0 
        
        while True:
            
            if empty >= numExchange:
                empty -= numExchange
                numExchange+=1 
                numBottles+=1 
            elif numBottles>0:
                drunk+= numBottles
                empty+= numBottles
                numBottles=0
            else:
                break
        return drunk 
    
    
obj = Solution()

a,b = 13,6
a,b = 10,3 
print(obj.maxBottlesDrunk(a,b))
    
    