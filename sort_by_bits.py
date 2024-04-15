'''
https://leetcode.com/problems/sort-integers-by-the-number-of-1-bits/
'''

class Solution:
    # what if arr has duplicate elements , it won;t work
    # def sortByBits(self, arr: list[int]) -> list[int]:
    #     mapper = {}
    #     for num in arr:
    #         mapper[num] = str(bin(num)).replace("0b", "").count('1')
    #     print(mapper)
    #     sorted_mapper = sorted(mapper.items(), key = lambda x: (x[1],x[0]))
    #     print(sorted_mapper)
    #     return [x[0] for x in sorted_mapper]

    # def sortByBits(self,arr):
    #     bucket = {}
    #     for num in arr:
    #         count = str(bin(num)).replace("0b", "").count('1')
    #         if count in bucket:
    #             bucket[count].append(num)
    #         else:
    #             bucket[count] = [num]
    #     print("Bucket ", bucket)
    #     result = []
    #     for  values in bucket.values():
    #         values.sort()
    #         result.extend(values)

    #     return result   

    def sortByBits(self, arr):
        return sorted(arr, key = lambda x : ((bin(x)[2:]).count('1'),x))



        


arr = [1024,512,256,128,64,32,16,8,4,2,1]
# arr = [2, 2]

obj = Solution()
print(obj.sortByBits(arr))
