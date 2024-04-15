'''
Standard Binary Search 
Return index of element if found else -1 

Input: nums = [-1,0,3,5,9,12], target = 9
Output: 4
Explanation: 9 exists in nums and its index is 4

'''


def binary_search(nums,target):

    start = 0 
    end = len(nums)-1

    while start <= end :
        mid = start + (end-start)//2
        if nums[mid] == target:
            return mid 
        
        if nums[mid]>target:
            end = end - 1
        elif nums[mid] < target:
            start = start+1

    return -1 

nums = [-1,0,3,5,9,12]
target = 9 

nums1= [1, 3, 5, 7, 9]
target = 6

nums1 = [1,3,5,7,9]
target = 5
print(binary_search(nums1, target))
