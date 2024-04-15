'''
Given unordered list of intergers in the range [1,n] where n = len(nums)+2 
find two missing number in sorted orders 
ex:[1,4,3], len(nums)=3 -> range = [1,5] so missing = [2,5]
'''

'''
Approach 1 : Using bitmap (works even if there are more than 2 nos missing in array )
We can use bitmap for checking which number is present in the range [1, n]
We will set bitmap = N & 0 (so that all bits are set 0)
then we will set bits at each index for the numbers in the array using "bitmap |= 1<<x" 
and then verify it using at the last " bitmap & (1<<x) ==0" to find which one of them are not set.


Approach 2: Mathematical approach 
Let 'a' and 'b' be two missing numbers 
Sum(1,N) - Sum(arr) = a+b 
SumOfSquares(1,N) - SumOfSquares(arr) = a**2 + b**2 

so we have linear equation in hand to solve for a, b 
solve it to get 
a*b =  ( (a+b)**2 - (a**2-b**2))/2

replace a with b- [Sum(1,N) - Sum(arr)] to solve above equation 

'''

def missingNumbers(nums):
    # Write your code here.
    
    missing_nos = []
    N = len(nums) + 2
    bitmap = N & 0 
    for num in nums:
        bitmap |= 1 << num 
    
    print(bin(bitmap))
    #check for unset bits 
    for i in range(1, N+1):
        if bitmap & (1<<i) == 0:
            missing_nos.append(i)


    return missing_nos


def find_missing_numbers_maths_approach (arr):
    N = len(arr) + 2

    # Expected sum and sum of squares
    expected_sum = N * (N + 1) // 2
    expected_sq_sum = N * (N + 1) * (2 * N + 1) // 6



    # Actual sum and sum of squares
    actual_sum = actual_sq_sum = 0
    for num in arr:
        actual_sum += num
        actual_sq_sum += num ** 2

    # Calculate the differences
    sum_diff = expected_sum - actual_sum
    sq_sum_diff = expected_sq_sum - actual_sq_sum

    print(sum_diff)
    print(sq_sum_diff)

    # Solving the equations
    # x + y = sum_diff
    # x^2 + y^2 = sq_sum_diff
    # => x^2 + (sum_diff - x)^2 = sq_sum_diff
    # Solving the quadratic equation
    A = 2
    B = -2 * sum_diff
    C = sum_diff**2 - sq_sum_diff

    # Calculate discriminant
    discriminant = B**2 - 4 * A * C
    x1 = (-B + discriminant**0.5) / (2 * A)
    x2 = (-B - discriminant**0.5) / (2 * A)

    return sorted([int(x1), int(x2)])





nums = [1,4,3]
print(find_missing_numbers_maths_approach(nums))