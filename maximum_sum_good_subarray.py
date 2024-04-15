'''
https://leetcode.com/contest/biweekly-contest-123/problems/maximum-good-subarray-sum/

O(N*N) solution is to try out all the index pairs (i,j) and keep the sum of them, return maximum sum 
'''

#Brute Force Solution 
def maximumSubarraySum(nums, k):
    maxSum = None
    for i in range(len(nums)-1):
        localSum = nums[i]
        for j in range(i+1, len(nums)):
            localSum += nums[j]
            if abs(nums[i]-nums[j]) == k:
                if maxSum :
                    maxSum = localSum if maxSum<localSum else maxSum
                else:
                    maxSum = localSum
    
    return maxSum if maxSum else 0 


#  Working solution but O(N*N) solution 
def maximumGoodSubArraySum(nums, k):
    mapper = {}
    maxSum = None

    prefixSum = [0]
    for num in nums:
        prefixSum.append(prefixSum[-1]+num)

    for i, ele in enumerate(nums):
        first, second = ele+k, ele-k 
        print("i : {}, ele: {}".format(i, ele))
        print("first: {},  second: {}".format(first, second))
        localSum = None
        if ele in mapper:
            for start_index in mapper[ele]:
                localSum = prefixSum[i+1] - prefixSum[start_index]
                print("LocalSum : {}".format(localSum))
                if maxSum is None:
                    maxSum = localSum
                else:
                    maxSum = max(localSum, maxSum)

                print("MaxSum : {}".format(maxSum))


        if first not in mapper:
            mapper[first] = [i]
        else:
            mapper[first].append(i)
        
        if second not in mapper:
            mapper[second] = [i]
        else:
            mapper[second].append(i)


    print(mapper)
    print(maxSum)


def maximumGoodSubArraySumGPT(nums, k):
    mapper = {}
    maxSum = None
    prefixSums = [0]  # Initialize prefix sums with 0 to handle sum calculation from the start

    # Compute prefix sums
    for num in nums:
        prefixSums.append(prefixSums[-1] + num)

    # Iterate through the array to find all good subarrays
    for i, num in enumerate(nums):
        for target in (num + k, num - k):
            if target in mapper:
                for start_index in mapper[target]:
                    # Calculate the sum using the prefix sums array
                    currentSum = prefixSums[i + 1] - prefixSums[start_index]
                    if maxSum is None:
                        maxSum = currentSum
                    else:
                        maxSum = max(maxSum, currentSum)
        
        # Append the current index to the list of indices for the current number
        if num not in mapper:
            mapper[num] = []
        mapper[num].append(i)

    return maxSum if maxSum is not None else 0 


'''
This O(N) solution as we don't visit any element twice. 
Earlier in a map we were keeping all indices matching to target = nums[i] +/- k 
In case of duplicate values, this would be O(n*n)

For subarray nums[i->j] , sum = prefix[j+1] - prefix[i] ...eq(1)
where prefix[k] = sum of all elements before kth index where prefix[0] = 0 always 

Now to maximise eq(1) for the j, we need to minimize the prefix[i] for every j 
So for every value in Array,if we store the minimum prefix sum for that value in mapper, then prefix[i] can be obtained in O(1) time 
which is guaranteed to be smallest for given j 

So mapper[nums[j]] = min(mapper[nums[j]], prefix[j]) 

Answer would be simply 
exp1 = nums[j]+k 
ans = max(ans, prefix[j+1]-mapper[exp1]) , where exp1 == nums[i]

-- same for exp2 

Now,for each past index we would just store the minimum value for that index value prefixc sum 
ex: for [3,3,2]
prefix = [0,3,6,8]
mapper[nums[0]] = mapper[3] = 0 
mapper [nums[1]] = mapper[3] =  min(mapper[nums[1]], prefix[1-1]) = min(0, 0) = 0 # storing minimum prefix sum for that value 
mapper[nums[2]] = mapper[2] = 6

Reference : https://www.youtube.com/watch?v=zFxDDglHb4o 
'''
def maxGoodSubArraySum(nums, k):
    maxSum = -10**20 
    mapper = {} # to hold the minimum prefix sum of all target indices 
    prefixSum = [0] 
    for num in nums:
        prefixSum.append(prefixSum[-1]+num)

    for j in range(len(nums)):
        expectedValue1 = nums[j]-k 
        expectedValue2 = nums[j]+k 

        if expectedValue1 in mapper:
            maxSum = max(maxSum, prefixSum[j+1]-mapper[expectedValue1])
        if expectedValue2 in mapper:
            maxSum = max(maxSum, prefixSum[j+1]-mapper[expectedValue2])

        # Update the mapper for current sum 
        # prefix[i] --> sum of all indices before i 
            
        if nums[j] in mapper:
            mapper[nums[j]] = min(mapper[nums[j]], prefixSum[j])
        else:
            mapper[nums[j]] = prefixSum[j]

    return maxSum if maxSum != -10**20 else 0


def maxGoodSubArraySum(nums, k):
    # Initialize the maximum subarray sum to a very small number to ensure any positive result will be larger.
    maxSum = -10**20
    # Initialize a dictionary to store the minimum prefix sum encountered for each unique number in 'nums'.
    mapper = {}
    # Initialize a list to store the prefix sums, starting with 0 to simplify sum calculations.
    prefixSum = [0]
    for num in nums:
        # Calculate prefix sums iteratively and append to 'prefixSum'.
        prefixSum.append(prefixSum[-1] + num)

    for j in range(len(nums)):
        # Calculate the expected values that could form a 'good subarray' with 'nums[j]'.
        expectedValue1 = nums[j] - k
        expectedValue2 = nums[j] + k

        # If an expected value is found in 'mapper', it means a 'good subarray' can end at 'j'.
        # Update 'maxSum' by considering the difference between 'prefixSum[j+1]' and the minimum prefix sum stored in 'mapper'.
        if expectedValue1 in mapper:
            maxSum = max(maxSum, prefixSum[j+1] - mapper[expectedValue1])
        if expectedValue2 in mapper:
            maxSum = max(maxSum, prefixSum[j+1] - mapper[expectedValue2])

        # Update 'mapper' with the current number. The goal is to store the smallest prefix sum encountered so far for each number.
        # This ensures that when calculating the sum of a 'good subarray', the smallest possible value is subtracted, maximizing the subarray sum.
        if nums[j] in mapper:
            mapper[nums[j]] = min(mapper[nums[j]], prefixSum[j])
        else:
            mapper[nums[j]] = prefixSum[j]

    # Return the maximum subarray sum found; if none are found, return 0.
    return maxSum if maxSum != -10**20 else 0


# nums = [-1,3,2,4,5]
# k = 3
# ans = 11

# nums = [-1,2,-3,-4,5,4,-1]
# k = 2
# ans = 4
    
nums = [1,2,3,4,5,6]
k = 1
#ans = 11

nums = [-677,-599,-452,-340,-561,-402,-741,-373,-1000,-842,-355,-717,-556,-196,-126,-511,-174,-424,-569,-566,-161,-438,-402,-915,-709,-797,-377,-731,-380,-975,-601,-280,-629,-171,-558,-626,-857,-942,-223,-632,-950,-449,-136,-865,-350,-791,-781,-271,-953,-912,-100,-775,-938,-576,-268,-230,-269,-393,-844,-897,-828,-498,-598,-344,-775,-187,-437,-797,-311,-287,-978,-334,-961,-264,-323,-282,-659,-980,-622,-701,-116,-277,-861,-562,-647,-183,-856,-372,-111,-624,-514,-252,-275,-430,-273,-323,-774,-535,-797,-291]
k = 53
#ans = -1741

# nums = [3,3,2]
# k = 1
print(maxGoodSubArraySum(nums,k))