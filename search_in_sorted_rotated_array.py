'''
https://leetcode.com/problems/search-in-rotated-sorted-array/description/


We use information of Sorting to solve this in O(logN)

# left sorted ? 
    if arr[start] < = arr[mid] & arr[start] < = key < = arr[mid] --> Search in left 

# right sorted ?
    if arr[mid] < = arr[end] & arr[mid] < = key < = arr[end]  --> Search right 



'''

def search_in_sorted_rotated_array(nums, target, start, end):
    if start <= end: 

        mid = start + (end-start)//2
        if nums[mid] == target:
            return mid 
        
        #left sorted  ?
        if nums[start] <= nums[mid] :
            #left sorted 
            if nums[start] <= target < nums[mid] :
                return search_in_sorted_rotated_array(nums, target, start, mid-1)
            else:
                return search_in_sorted_rotated_array(nums, target, mid+1, end) 
        elif nums[mid] <= nums[end] :
            #right sorted
            if nums[mid] < target <= nums[end]:
                return search_in_sorted_rotated_array(nums , target, mid+1, end)
            else:
                return search_in_sorted_rotated_array(nums , target, start, mid-1)
        
        
        
    return -1 


def search(nums, target):
    start  = 0 
    end = len(nums)-1
    return search_in_sorted_rotated_array(nums, target, start, end)



nums = [4,5,6,7,0,1,2]
target = 1

# nums = [5,1,3]
# target =5 

print(search(nums, target))