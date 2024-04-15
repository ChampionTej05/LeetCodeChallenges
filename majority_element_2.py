'''
leetcode: https://leetcode.com/problems/majority-element-ii/

Extended Boyer-Moore Voting Algorithm 

This gives potential candidates which could exists more [n/3] times 
Verify using counter, if both are correct or one of them is correct 
'''

def majorityElement(nums):
    candidate1, candidate2 = None, None 
    counter1,counter2= 0, 0 

    for ele in nums: 
        if ele == candidate1:
            counter1+=1
        elif ele == candidate2:
            counter2+=1
        elif counter1==0:
            candidate1=ele 
            counter1=1
        elif counter2==0:
            candidate2=ele 
            counter2 =1 
        else:
            #element is not potential candidate yet 
            counter1-=1 
            counter2-=1 

    #verify potential candidates here now 

    print("Potential candidates " + str(candidate1) + ", " + str(candidate2))

    candidate1_counter , candidate2_counter = 0, 0 

    for ele in nums:
        if ele == candidate1:
            candidate1_counter+=1
        elif ele == candidate2:
            candidate2_counter+=1 

    results = set()
    N = len(nums)
    print("counters "+ str(candidate1_counter) + ", " + str(candidate2_counter))
    if candidate1_counter > N//3:
        results.add(candidate1)
    if candidate2_counter > N//3:
        results.add(candidate2)

    return list(results)


arr = [1, 2, 2, 3, 2, 1, 1, 3]
arr = [1,1,1,3,3,2,2,2]
print(majorityElement(arr))