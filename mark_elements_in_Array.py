'''
https://leetcode.com/contest/biweekly-contest-126/problems/mark-elements-on-array-by-performing-queries/
'''


class Solution(object):
    
    
    
    def unmarkedSumArray(self, nums, queries):
        """
        :type nums: List[int]
        :type queries: List[List[int]]
        :rtype: List[int]
        """
        import heapq
        N = len(nums)
        mapper = [ False for i in range(N)]
        
        h = [(n,i) for i, n in enumerate(nums)]
        heapq.heapify(h)
        
        print("heap ", h)
        total_sum = sum(nums)
        answer = []
        for query in queries:
            
            idx , k = query 
            
            if not mapper[idx]:
                total_sum-= nums[idx]
                mapper[idx] = True 
                
            # get k small elements which are unmarked 
            i =0
            while i<k:
                if len(h) == 0:
                    break
                ele, index = heapq.heappop(h)
                print("ele, index", ele, index)
                if mapper[index]:
                    continue 
                mapper[index]  = True 
                total_sum -= ele 
                i+=1 
                
            print("total sum after query : ", query, total_sum)
            print("Heap status", h)
            print("marker ", mapper)
            answer.append(total_sum)
            
        return answer
     
nums = [1,2,2,1,2,3,1]
queries = [[1,2],[3,3],[4,2]]

nums = [1,4,2,3]
queries = [[0,1]]

nums = [1,2,2,1,5,3,1,5,1,1,5,2]

queries = [[1,10],[3,3],[4,10]]

obj = Solution()
print(obj.unmarkedSumArray(nums, queries ))               
            
            
                
        