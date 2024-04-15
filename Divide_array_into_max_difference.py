'''
https://leetcode.com/problems/divide-array-into-arrays-with-max-difference/description/?envType=daily-question&envId=2024-02-01
'''


def divideArray(nums, k):

    results = []
    nums.sort()

    N = len(nums)

    for i in range(0,N,3):
        subarray = nums[i:i+3]
        if subarray[-1] - subarray[0] <=k:
            results.append(subarray)
        else:
            return []
        
    return results
        