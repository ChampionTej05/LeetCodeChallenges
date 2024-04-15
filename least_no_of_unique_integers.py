'''
https://leetcode.com/problems/least-number-of-unique-integers-after-k-removals/?envType=daily-question&envId=2024-02-08
'''

class Solution(object):
    def findLeastNumOfUniqueInts(self, arr, k):
        """
        :type arr: List[int]
        :type k: int
        :rtype: int
        """
        
        
        
        from collections import defaultdict
        
        counter = defaultdict(int)
        
        for ele in arr:
            counter[ele]+=1 

        counter = sorted(counter.items(), key = lambda x: x[1])
        print(counter)
        
        elements_removed = 0 
        unique_elements_array = len(set(arr))
        for key, value in counter:
            if k >= elements_removed:
                count_removed = min(k-elements_removed, value)
                print("For Key : {}, count removed : {}".format(key, count_removed))
                elements_removed += count_removed 
                
                if count_removed == value:
                    unique_elements_array-=1
            else:
                break 
            
            
        print(counter)
        print("Unique Elements left: ", unique_elements_array)
            
            
        
        




arr = [2,4,1,3,1,3,3]
obj = Solution()

obj.findLeastNumOfUniqueInts(arr, 3)        