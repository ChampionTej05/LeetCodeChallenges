

'''
Validate if the given array is sub sequence of the target array 
Subsequence of array is given by : set of numbers from target that are not necessarily adjacent 
but should be in the same order.
Single number and array itself is valid subsequence 
ex: [1,2,3] , subsequence = {[1], [1,2], [1,3], [2], [2,3], [3], [1,2,3]}
'''


def isValidSubsequence(array, sequence):
    # Write your code here.
    
    arrayPtr = 0
    sequencePtr = 0

    while arrayPtr < len(array) and sequencePtr < len(sequence):
        if array[arrayPtr] == sequence[sequencePtr]:
            sequencePtr=sequencePtr+1
        arrayPtr= arrayPtr+1

    if sequencePtr == len(sequence):
        return True 

    return False 



array = []
sequence = []

print(isValidSubsequence(array, sequence))