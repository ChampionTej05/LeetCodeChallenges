def isMonotonic(array):
    # Write your code here.
    if len(array) <=1:
        return True

    #find first element which is not equal to start of the array 
    first_element = array[0]
    idx = 0
    while idx < len(array) and first_element == array[idx]:
        idx=idx+1
    
    #all elements are same 
    if idx == len(array):
        return True 
    trend = array[idx]-first_element 
    if trend >0:
        #all should non-decreasing 
        for i in range(idx+1, len(array)):
            if array[i] - array[i-1] < 0:
                return False 
    else:
        # all should be non-increasing 
        for i in range(idx+1, len(array)):
            if array[i] - array[i-1] > 0:
                return False 
    return True

def isMonotonicV1(arr):
    if len(arr) < 2:
        return True

    trend = -1
    #  0 --down , 1 --up
    for i in range(len(arr) - 1):

        if arr[i] > arr[i + 1]:
            # set trend to down but first check if it was up or not
            if trend == 1:
                return False
            trend = 0
        elif arr[i] < arr[i + 1]:
            if trend == 0:
                return False
            trend = 1
    return True
            
arr = [-1, -5, -10, -1100, -1100, 1101, -1102, -9001]
print(isMonotonic(arr))
