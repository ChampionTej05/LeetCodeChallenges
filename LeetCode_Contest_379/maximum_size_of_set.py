'''
https://leetcode.com/contest/weekly-contest-379/problems/maximum-size-of-a-set-after-removals/

We need to maximize the size of set --> Find maximum unique elements across two sets 

1. Get the count of each element 
2. First remove all repetivie elements from each array 
3. If after this, still there are more than n/2 elements left in the array, we need to remove elements with respect to the array 
4. Remove elements which are common in both arrays 
5. At last, even if the length of the array does not go beyond n/2, we remove elements till length = n/2


Read this awesome solution : https://leetcode.com/problems/maximum-size-of-a-set-after-removals/solutions/4520990/c-java-python-set-difference/

# one more great solution on simialr lines 
    def maximumSetSize(self, nums1: List[int], nums2: List[int]) -> int:
        N = len(nums1)
        nums1, nums2 = set(nums1), set(nums2)
        both = nums1 & nums2 # common in both
        one = nums1 ^ both # unique elements in num1 but not in nums2
        two = nums2 ^ both # unique elements in nums2 but not in nums1 
        from_one = min(N//2, len(one)) # how many unique elements should we includes from nums1 
        from_two = min(N//2, len(two)) # how many unique elements should we includes from nums2
        return min(from_one + from_two + len(both), N) # len(both) is added if from_one + from_two still doesn't add upto N i.e. unique elements from both related to respective arrays are not enough to satisfy n//2 
'''


nums1 = [1,2,2,2,3,4,6,6,8,9]
nums2= [1,1,1,1,3,3,3,3,4,8,9,9,9,9]

nums1 = [1,2,3,4,5,6]
nums2 = [2,3,2,3,2,3]

nums1 = [1,1,2,2,3,3]
nums2 = [4,4,5,5,6,6]


def maximumSetSize(nums1, nums2):
    from collections import Counter
    n1 = len(nums1)
    values_to_remove_1 = n1//2
    n2 = len(nums2)
    values_to_remove_2 = n2//2

    most_common_elements = Counter(list(set(nums1)) + list(set(nums2))).most_common()

    #  remove duplicates directly from the array (as they won't give much value to the size(set))
    nums1 = list(set(nums1))
    nums2 = list(set(nums2))
    cnt1  = Counter(nums1)
    cnt2 = Counter(nums2)
    for value, count in most_common_elements:
        # This element occurs most of the time in both elements,
        # We need to remove this element where N/2 condition is not met yet 
        if len(nums1) > values_to_remove_1:
            if cnt1[value]>0:
                nums1.remove(value)
                cnt1[value]-=1 
                    
        elif len(nums2) > values_to_remove_2:
            if cnt2[value]>0:
                nums2.remove(value)
                cnt2[value]-=1

        if len(nums1) == values_to_remove_1 and len(nums2) == values_to_remove_2:
            break 

    max_set_size = len(set(nums1+nums2))
    # print(max_set_size)
    return max_set_size

            


    








