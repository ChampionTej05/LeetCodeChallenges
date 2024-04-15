'''
Kadane's Algorithm 
'''


def maxSumSubarray(nums):
    if len(nums)==1:
        return nums[0]
    max_sum = nums[0]
    current_sum = nums[0]

    for ele in nums[1:]:
        if current_sum + ele > ele:
            current_sum +=ele
        else:
            current_sum = ele 
        max_sum = max(max_sum, current_sum)
    
    return max_sum

'''
Divide and Conquer Approach (nLogn) 
MaxSum = maxSum(left) + maxSum(right)+maxSumCrossingMid
maxSumCrossingMid -> Subarray sum which cross mid and present across mid 

Correct Approach for Finding the Maximum Crossing Subarray
Start from the Middle: The crossing subarray must include elements from both the left and right halves of the array, and it must cross the midpoint.

Expand Left and Right:

Left Side: Start at the mid index and expand leftward. Accumulate the sum of elements and keep track of the maximum sum found as you move left. This finds the maximum sum subarray starting from the middle and expanding to the left.
Right Side: Similarly, start just right of mid (i.e., at mid + 1) and expand rightward, keeping track of the maximum sum found as you move right. This finds the maximum sum subarray starting from just right of the middle and expanding to the right.
Combine the Left and Right Sums: The maximum sum for the crossing subarray is the sum of the maximum sums found on the left and right sides.


'''

def maxSumSubArrayDivideAndConquer(nums, start, end ):
    if start == end :
        return nums[start] #base case 
    
    mid = start + (end-start)//2
    print("nums : {}, start: {}, end : {}, mid: {}".format(nums[start:end], start, end, mid))
    
    #recur here 
    maxSumInLeft = maxSumSubArrayDivideAndConquer(nums, start, mid)
    maxSumInRight = maxSumSubArrayDivideAndConquer(nums,mid+1, end) if mid+1 <len(nums)  else 0
    maxSumCrossingMid = findMaxSumCrossingMid(nums,start,mid,end)

    print("leftSum : {}, rightSum: {}, crossingSum: {}".format(maxSumInLeft, maxSumInRight, maxSumCrossingMid))

    return max(maxSumInLeft, maxSumInRight, maxSumCrossingMid)

def findMaxSumCrossingMid(nums, start, mid, end):
    import sys 

    print("Crossing -> nums : {}, start: {}, end : {}, mid: {}".format(nums[start:end], start, end, mid))
    leftSum , currentSum = -sys.maxsize ,0
    for i in range(mid, start-1, -1):
        currentSum+=nums[i]
        leftSum = max(leftSum, currentSum)

    print("leftSum : {}".format(leftSum))
    
    rightSum, currentSum = -sys.maxsize , 0 
    #mid+1 because mid is already calculated in left sum 
    for i in range(mid+1, end, 1):
        currentSum += nums[i]
        rightSum = max(rightSum, currentSum)

    print("rightSum : {}".format(rightSum))
    return leftSum+rightSum

def maxSumSubarray(nums):

    N=len(nums)
    result = maxSumSubArrayDivideAndConquer(nums, start=0,end=N)
    print(result)
    return result 

nums = [-2,1,-3,4,-1,2,1,-5,4]

assert 6 == maxSumSubarray(nums)