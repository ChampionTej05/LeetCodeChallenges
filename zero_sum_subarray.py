'''
Check if there exists subarray with sum =0 in array
'''

def zeroSumSubarray(nums):
    # Write your code here.
    if len(nums)<0:
        return False
    
    if len(nums) == 1 :
        return nums[0] ==0 
    prefix_sum = nums[0]
    mapper= {}
    mapper[prefix_sum] = 0 
    for i in range(1, len(nums)):
        prefix_sum += nums[i]
        if prefix_sum ==0:
            print("arr found", nums[:i+1])
            return True 
        if prefix_sum in mapper:
            print("Equal arr found ", nums[mapper[prefix_sum]:i+1])
            return True 
        mapper[prefix_sum] = i 

    print("Prefix Sum ", prefix_sum)
    return False 


nums = [3, 4, -7, 3, 1, 3, 1, -4, -2, -2]
nums = [-5,-5, 2,3,-2]
print(zeroSumSubarray(nums))
    