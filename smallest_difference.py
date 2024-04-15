
import sys
def smallestDifference(arrayOne, arrayTwo):
    # Write your code here.
    arrayOne.sort()
    arrayTwo.sort()

    i =  0 
    j = 0 
    global_min = sys.maxsize
    result = []
    while i < len(arrayOne) and j < len(arrayTwo):
        current_sum = abs(arrayOne[i]-arrayTwo[j])
        if current_sum == 0:
            return [arrayOne[i], arrayTwo[j]]
        if current_sum < global_min:
            global_min = current_sum
            result = [arrayOne[i], arrayTwo[j]]
        
        if arrayOne[i] < arrayTwo[j]:
            i+=1
        elif arrayOne[i] > arrayTwo[j]:
            j+=1

    
    return result 
        



arrayOne= [-1, 5, 10, 20, 28, 3]
arrayTwo = [26, 134, 135, 15, 17]
result = smallestDifference(arrayOne, arrayTwo)
print(result)
