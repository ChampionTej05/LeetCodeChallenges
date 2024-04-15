'''
https://leetcode.com/problems/find-the-duplicate-number/

O(1) space 
'''
class Solution:
    def findDuplicate(self, nums: list[int]) -> int:
        N = len(nums)
        bitmap = N & 0 

        for i in range(N):
            if bitmap & (1 << nums[i]) !=0: 
                print("Duplicate Found : ", nums[i])
                return nums[i]
            else:
                bitmap |= 1<<nums[i]
            print("Bitmap : ", bin(bitmap))

    def findUsingCounter(self,nums):
        from collections import Counter 

        cnt = Counter(nums)
        return cnt.most_common()[0][0]

obj = Solution()

nums = [1,3,4,2,2]

print(obj.findUsingCounter(nums))
