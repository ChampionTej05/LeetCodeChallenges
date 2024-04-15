def custom_bisect_right(arr, element):
    low, high = 0, len(arr)

    while (low<high):
        mid = low + (high-low)//2
        if arr[mid] <= element:
            low = mid + 1 # if arr[mid]==element, answer would be always on right, hence not low=mid 
        else:
            high = mid # not high=mid-1 because mid could be one of the answer being next right element 

    return low # when single element is left, low is pointing to right element 


arr = [69,71,72,73,73,74,75,76]
print(custom_bisect_right(arr, 72))