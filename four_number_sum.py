
#Each function expects the array to be in sorted order 

def two_number_sum(array, target):

    left = 0 
    right = len(array)-1
    pairs = []
    while left < right:
        current_sum = array[left] + array[right]

        if current_sum == target:

            pair = [array[left], array[right]]
            pairs.append(pair)

            # skip duplicate 

            while left< right and array[left] == array[left+ 1]:
                left= left + 1 

            while left < right and array[right] == array[right-1]:
                right = right -1 


            # move to next value as current pointer is same as before
            left = left + 1
            right = right -1 

        elif current_sum < target:
            left = left +1 
        else:
            right = right -1 

    return pairs 

def three_number_sum(array,target):

    left = 0 
    right = len(array)-1 
    results = list()


    for i in range(len(array)-1):
        #skip duplicate numbers
        if i>0 and array[i] == array[i-1]:
            continue

        pairs = two_number_sum(array[i+1:], target-array[i])
        if pairs:
            new_pairs = [[ array[i], pair[0], pair[1]] for  pair in pairs]
            results.extend(new_pairs)
            

    

    # remove duplicates 
    aset = set()
    triplet_results= []
    for triplet in results:
        atuple = tuple(triplet)

        if atuple in aset:
            continue
        else:
            aset.add(atuple)
            triplet_results.append(triplet)


    return triplet_results

#give duplicatevalue 
def four_number_sum(array , target):
    results = []
    for i in range(len(array)-2):

        #skip first duplicate number
        if i>0 and array[i] == array[i-1]:
            continue

        triplets = three_number_sum(array[i+1:], target-array[i])
        print(triplets)
        if triplets:
            new_triplets = [[array[i], trip[0], trip[1], trip[2]] for trip in triplets]
            results.extend(new_triplets)

        print("----------")
            


    
    return results


def four_number_sum_non_duplicate(nums, target):

    result = []
    n = len(nums)

    for i in range(n):
        # Avoid duplicate values for the first number
        if i > 0 and nums[i] == nums[i - 1]:
            continue

        for j in range(i + 1, n):
            # Avoid duplicate values for the second number
            if j > i + 1 and nums[j] == nums[j - 1]:
                continue

            left, right = j + 1, n - 1
            while left < right:
                sum = nums[i] + nums[j] + nums[left] + nums[right]
                if sum == target:
                    result.append([nums[i], nums[j], nums[left], nums[right]])
                    
                    # Skip duplicates for the third and fourth numbers
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1

                    left += 1
                    right -= 1
                elif sum < target:
                    left += 1
                else:
                    right -= 1

    return result   

# array = [2,4,1,5,7,-1]
# target = 6


# array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 15]
# target = 18



array = [1, 2, 3, 4, 5, -5, 6, -6]
target = 5

array.sort()
print("array ", array)
print(four_number_sum(array, target))





