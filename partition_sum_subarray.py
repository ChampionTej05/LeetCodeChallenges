'''
https://leetcode.com/problems/partition-array-for-maximum-sum/description/?envType=daily-question&envId=2024-02-03

Intuition is to do it recursively 

We create subarray of length 1,2,.. K and for each subarray created we call recursive function for remaining array 

Reference : https://www.youtube.com/watch?v=eVN10YAMSJU
'''


def recursive_caller(arr, starting_index, k, dp ):
    # if it is out of bound, sum is 0 always
    if starting_index >= len(arr): 
        return 0 
    if dp[starting_index] != -1 : 
        return dp[starting_index]


    i = starting_index 
    current_length_of_subarray = 1
    maximum_element_in_subarray = -1 # as all are positive integers
    maximum_array_sum = 0
    while ( i < starting_index+k and i < len(arr)):
        
        maximum_element_in_subarray = max(maximum_element_in_subarray, arr[i])
        ele_value = (current_length_of_subarray*maximum_element_in_subarray)
        rs_value = recursive_caller(arr,i+1, k, dp)
        largest_sum_for_array = ele_value + rs_value
        # print("i", i)
        # print("ele value", ele_value)
        # print("Arr would be : ", [maximum_element_in_subarray]*current_length_of_subarray)
        # print("Largest sum afte this arr : ", largest_sum_for_array)
        # print("rs value", rs_value)
        maximum_array_sum = max(maximum_array_sum, largest_sum_for_array)

        current_length_of_subarray+=1
        i+=1
    dp[starting_index] = maximum_array_sum
    return dp[starting_index]


def maxSumAfterPartitioning(arr, k):
    dp = [-1]*len(arr)
    return recursive_caller(arr, 0, k, dp)

arr = [1,15,7,9,2,5,10]
k = 3

# arr = [5, 10]
# k = 3
        
print(maxSumAfterPartitioning(arr, k))