'''
Majority element : Element that exists more [n/2] times in the array 


Solution :
Approach 1 : using boyer-moore voting algorithm 
Boyer-Moore Voting Algorithm Concept
Intuition: If we had some way of counting instances of the majority element as +1 and instances of any other element as -1, then the sum of all counts would never be negative.

Initial Setup:
Start with two variables: one to store a potential candidate for the majority element and another for a counter, initially set to 0.
Iterate Through the Array:

For each element in the array:
If the counter is 0, set the current element as the potential candidate.
If the current element is equal to the candidate, increment the counter.
If the current element is different from the candidate, decrement the counter.
Majority Element:

After iterating through the entire array, 
the candidate will be the majority element. 
This works because the majority element's count will always overpower the count of any other element, 
ensuring that the candidate remains the majority element at the end of the array.

Why it Works: The key insight is that every time the counter is set to 0, it means that up to that point, there is no majority element. 
However, since we know that a majority element exists (which appears more than ⌊n / 2⌋ times), it will eventually emerge as the counter increases.
'''

# this will work only if there is guarantee that majority element exists in the array 
def majorityElement(array):
    # Write your code here.
    potential_candidate = None
    potential_candidate_counter = 0

    for ele in array:
        
        if potential_candidate_counter ==0:
            potential_candidate = ele 

        if ele == potential_candidate :
            potential_candidate_counter +=1
        else:
            potential_candidate_counter -=1 
        print("candidate : {}, counter : {}, current element: {}".format(potential_candidate, potential_candidate_counter, ele))

    if potential_candidate_counter < 0:
        print("Majority Element did not exists ")
        return -1 
    return potential_candidate

nums = [1,2,3,2,2,3,1,1,1,2,2,0,0,0,0,0,0,0]
nums = [1,2,3,2,2]

print(majorityElement(nums))