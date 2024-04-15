def permute(nums):
    def backtrack(start, end):
        if start == end:
            result.append(nums[:])
        for i in range(start, end):
            # Swap
            nums[start], nums[i] = nums[i], nums[start]
            # Recurse
            backtrack(start + 1, end)
            # Backtrack
            nums[start], nums[i] = nums[i], nums[start]

    result = []
    backtrack(0, len(nums))
    return result

# Example usage
nums = [i for i in range(1, 50)]
permute(nums)
# print()

# nums = [1,3,2]
# print(permute(nums))
