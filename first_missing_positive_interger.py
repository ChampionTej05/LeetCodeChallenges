'''
https://leetcode.com/problems/first-missing-positive/description/?envType=daily-question&envId=2024-03-25

Cyclic Sort 
(If we sort the elements , then element which does not follow property of nums[i] == i+1 , will be answer)
(Our answer will always be in the range of (1,N+1) N = len(nums) always using piegon hole principle 
N slots are present in the array to place numbers, the minimum possible number which can be missing is 1 (positive number is asked)
Maximum can not go beyond N+1, because if number greater than N+1 is present in the array, then it at least one element in the range (1,N) is removed to accomodate that
So that removed element will be our answer, --> Answer range (1, N+1))

Every number x=nums[i], should be at index = x-1 ==> x = index+1 ==> nums[i] == i + 1 (if at expected position)

So if the current index "i" we are checking 
    a. If the elements at current index, is within our range of [1,N] ? ( So that we don't unnecessarily get index out of bound situation and try to map answer candidates which won't be our answers) 
        check next index
    1. Is the element at current index, is at it's correct place ==> is nums[i] == i+1 ? 
    2. If not, then where this element suppose to go (nums[i]-1 index), is that element in correct place already (this is needed, so that we don't remove elements which are positioned correctly as per their indexes) ? nums[nums[i]-1] == (nums[i]-1)+1 [nums[i]-1 is the index and all elements are suppose to be index+1 value]
    3. If not, then SWAP (nums[i], nums[nums[i]-1])
    4. Repeat steps a to 3, newly introduced element at index "i" 
    5. If all of  1 to 3, is false 
        check next index 

Iterate through array and return the first element where nums[i]!=i+1
        
0   1   2   3    : Indexex
3   4   -1  1    : initial array 
-1  4   3   1    : i=0, x=3, 3 should have been at index=3-1=2 , also the element at index=2, nums[2]=-1 , is also not at correct position (-1 != (3-1)+1) = (-1 !=2) , SWAP(0, 2) index. 
                    After that, at i=0, -1 doesn't satisfy condition "a", so we skip and move to next index 
                    
-1  1   3   4    : i=1, x=4, SWAP(1,3). After this , in resultant array, at i=1, element is not at correct position because nums[i] !=i+1 and nums[nums[i]-1] != nums[i] (nums[0] != nums[1]) --> (that means i=1 element, is not at correct position and element where this should go, is also not at correct position, so we can swap safely)
1   -1  3   4       After that, we can skip as -1 doesn't satisfy condition "a"
                 : i=2, i=3 both satisfy all conditions , so we end 
                 
at index=1, nums[index]!=index+1 (-1 !=2) --> return index+1 = 2               

        
'''


class Solution(object):
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        N = len(nums)
        
        current_element = 0 
        
        while current_element < N:
            
            x= nums[current_element]
            if x<=0 or x>N:
                current_element+=1 
                continue 
            
            if x != current_element +1 and nums[x-1] != x:
                nums[current_element], nums[x-1] = nums[x-1], nums[current_element]
            else:
                current_element+=1 
                
        
        print("Array ", nums)
        
        for i in range(N):
            if nums[i]!=i+1:
                return i+1 
            
        return N+1
            
        
        