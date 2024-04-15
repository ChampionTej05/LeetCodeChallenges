def moveElementToEnd(array, toMove):

    start =0 
    end = len(array)-1 

    while start <=end:
        if array[start] ==toMove and array[end] != toMove:
            array[start],array[end] = array[end], array[start]
        
        if array[start] != toMove:
            start= start+1
        if array[end] == toMove:
            end = end -1 

    return array


def moveToElementWithRelative(nums, toMove):
    non_zero_index = 0  # Initialize a pointer to track the position of non-zero elements

    # Traverse the array and move non-zero elements to the front
    for i in range(len(nums)):
        if nums[i] != toMove:
            nums[i], nums[non_zero_index] = nums[non_zero_index], nums[i]
            non_zero_index += 1

    return nums


def test_moveElementToEnd():
    # Test case 1: Example with a single element to move
    array1 = [2, 1, 2, 2, 3, 4, 2]
    toMove1 = 2
    result1 = moveElementToEnd(array1, toMove1)
    assert set(result1) == set([1, 3, 4, 2, 2, 2, 2])  # All 2s moved to the end.

    # Test case 2: Example with no elements to move
    array2 = [1, 3, 5, 7]
    toMove2 = 2
    result2 = moveElementToEnd(array2, toMove2)
    assert set(result2) == set([1, 3, 5, 7])  # No 2s in the array.

    # Test case 3: Example with all elements to move
    array3 = [0, 0, 0, 0]
    toMove3 = 0
    result3 = moveElementToEnd(array3, toMove3)
    assert set(result3) == set([0, 0, 0, 0])  # All 0s already at the end.

    # Test case 4: Example with empty array
    array4 = []
    toMove4 = 1
    result4 = moveElementToEnd(array4, toMove4)
    assert set(result4) == set([])  # Empty array remains empty.

    # Test case 5: Example with multiple elements to move
    array5 = [3, 1, 2, 4, 2, 5, 2]
    toMove5 = 2
    result5 = moveElementToEnd(array5, toMove5)
    assert set(result5) == set([3, 1, 4, 5, 2, 2, 2, 2])  # All 2s moved to the end.

    print("All test cases passed!")

# Run the test function
# test_moveElementToEnd()


arr = [2, 1, 2, 2, 2, 3, 4, 2]

toMove = 2
print(moveToElementWithRelative(arr, toMove))

arr = [1,0,0,5,6,0,2]
toMove =0 
print(moveToElementWithRelative(arr, toMove))