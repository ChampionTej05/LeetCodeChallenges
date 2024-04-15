def sortedSquaredArray(arr):
    start = 0 
    end = len(arr) -1 
    brr = [0] * len(arr)
    current = end 
    while start <= end:
        if abs(arr[start]) < abs(arr[end]):
            brr[current] = arr[end]**2 
            end = end-1 
        else:
            brr[current] = arr[start]**2
            start = start +1 
        current = current -1

    print(brr)
    return brr 


    
def test_sortedSquaredArray():
    # Test case 1: Standard case with positive and negative numbers
    arr1 = [-4, -2, 0, 2, 4]
    result1 = sortedSquaredArray(arr1)
    assert result1 == [0, 4, 4, 16, 16]

    # Test case 2: All positive numbers
    arr2 = [1, 2, 3, 4, 5]
    result2 = sortedSquaredArray(arr2)
    assert result2 == [1, 4, 9, 16, 25]

    # Test case 3: All negative numbers
    arr3 = [-5, -4, -3, -2, -1]
    result3 = sortedSquaredArray(arr3)
    assert result3 == [1, 4, 9, 16, 25]

    # Test case 4: Mixed positive and negative numbers
    arr4 = [-3, -2, 0, 2, 3]
    result4 = sortedSquaredArray(arr4)
    assert result4 == [0, 4, 4, 9, 9]

    # Test case 5: Empty input list
    arr5 = []
    result5 = sortedSquaredArray(arr5)
    assert result5 == []

    print("All test cases passed!")

# Run the test function
test_sortedSquaredArray()

        
