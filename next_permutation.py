'''
https://leetcode.com/problems/next-permutation/

Logic currently:

1. Find the "i" where nums[i] < nums[i-1] , if no such "i" exists then return the reverse of the array simply 
2. Now again from right to left, find "j" such that nums[j] > nums[i]. This element is going to next bigger element in right part for our "i"
3. Swap nums[i] <-> nums[j] and now create smallest numbers from "i+1" .. end { Reverse the array[i+1] or sort the array}

If we can't find a swap in Step1 , return the minimum possible number out of the digits (just reverse the number)


Why Just reverse in step 3 
Nature of the Subarray: When you find the first index i from the right where nums[i] < nums[i+1], the subarray from [i+1] to the end of the array is in descending order. This is guaranteed by the process of finding i.
Effect of the Swap: After swapping nums[i] with the smallest number larger than it in the subarray (found by traversing from the right), the subarray [i+1] to the end still remains in a non-ascending (descending or equal) order.
Reversing to Get the Next Permutation: Since the subarray is already in descending order, reversing it will turn it into ascending order. This is exactly what we need to get the smallest possible number from those digits. Sorting an already descending array is essentially just reversing it.
Efficiency: Reversing an array is more efficient than sorting it. Since we know the array is already in descending order, a reverse operation achieves the desired result in linear time (O(n)), while sorting would typically be O(n log n).
'''

def find_next_permutation(nums:list[int]):
    if len(nums) == 1:
        return nums
    N = len(nums)
    swap_found = False 
    
    i = N-2
    
    while i>=0:
        if nums[i] < nums[i+1]:
            swap_found = True  
            break
        i -=1 
    
    if not swap_found:
        nums = nums [::-1]
        print(nums)
        return

    j = N-1 
    while j > i :
        #  if we keep equal then same number would be created, so always strict inequal value
        if nums[j]>nums[i]:
            break 
        j-=1
    
    # There could never be a case where element greater or equal than nums[i] not found , as nums[i+1] is always greater than nums[i]

    # swap i and j values 
        
    print("i and j ", i, j)
        
    nums[i], nums[j] = nums[j], nums[i]
    nums[i+1] = reversed(nums[i+1:])
    print(nums)

    return 


# nums = [1,2,3]
nums = [3,2,1]
# nums = [3,4,2,1] #[4, 1, 2, 3]
# nums = [2,4,1,3]
# nums = [4,9,2,5,2,8,5,1] #[4, 9, 2, 5, 5, 1, 2, 8]
nums = [9,5,8,7,1] # [9, 7, 1, 5, 8]
# nums = [9,7,8,5,1] # [9, 8, 1, 5, 7]
nums = [1,5,1]
find_next_permutation(nums)
# print(nums)