'''
https://leetcode.com/problems/median-of-two-sorted-arrays/

Expected O(log(M+N)) solution

Brute Force = O(M+N)

Hint : using binary search on smaller array ,
Reference : https://www.youtube.com/watch?v=q6IEA26hvXc 

ex: 
B = [1,2,4,5,7,8]
A = [1,3,6,7]

A -> always smaller array 

- In the new array, elements to the left of the MEDIAN would be less than or equal to it 
    , to the right will be greater than or equal to
- So MEDIAN basically partitions the new array 
- "half = len(M+N)//2" will be count of elements less or equal than MEDIAN 
- So if somehow , we could partition the arrays A & B and generate left half then , we could find median 

A ==> Smaller array 
L = 0, R = len(A)-1 , half = len(M+N)//2 

* Find MID of A , MID = L+R//2 
* So left partition of A is L..MID 
* right partition of B would be 0..(half-mid-2)  [-2 is needed to adjust the indexes properly, do any dry run to find out ]
* Validate if the partition is correct as per original array 
    ** partition would be valid if MAX(ALEFT) <= MIN(BRIGHT) and MAX(BRIGHT) <= MIN(ARIGHT), 
        this is because when ALEFT+BLEFT both would be merged, their MAX elements would be always less or equal to MIN of RIGHT in valid partition
    ** If YES, find median 
        K = M+N, if K%2==0 --> MEDIAN = Max(ALEFT, BLEFT) + MIN(BRIGHT, ARIGHT) // 2, if K%2==1 --> MEDIAN = MIN(BRIGHT, ARIGHT)
    ** If no, we need to adjust the L and R in A 
        --> If MAX(ALEFT) > MIN(BRIGHT) => I have taken more elements from A by mistake, I need to decrease elements from A 
            # R = MID-1 
        --> If MAX(BRIGHT) > MIN(ARIGHT) ==> I have to reduce elements in ARIGHT, so that MIN(ARIGHT) can be increased
            # L = MID+1 
            
            
** to handle corner cases of whether MAX(ALEFT) or MIN(ARIGHT) exists or not, we can keep , 
    float("-inf") as value of leftmost part of any left partition 
    float("inf") as value of rightmost part of any right partition 
    So that, if there doesn't exists in any element in any partition of array, we can always compare 
        


for ex: 
B = [1,2,4,5,7,8]
A = [1,3,6,7]
A+B = [1,1,2,3,4,5,6,7,7,8] LEFT = [1,1,2,3,4] RIGHT = [5,6,7,7,8], MEDIAN = MAX(LEFT)+MIN(RIGHT)//2  (if even ) else SIMPLY MIDDLE ELEMENT 

L = 0 , R = 3 , HALF = 5 
* MID = 1(index) ,  ALEFT = [1,3], BLEFT = [1,2,4], HALF-MID-2 => 5-1-2 => 2(index) --> index 0,1,2
* Valid Partition ? 
    ** MAX(ALEFT) = 3, MAX(BLEFT) = 4, MIN(BRIGHT) = 5, MIN(ARIGHT) = 6 
    ** all conditions match 
    ** MEDIAN = MAX(3,4) + MIN(5,6) // 2 = 4+5 // 2 = 4.5
    
    
In the above case, let us say A = A = [1,6,6,7] B = [1,2,4,5,7,8]  , A+B = [1,1,2,4,5,6,6,7,7,8]
L = 0 , R = 3 , HALF = 5
* MID = 1, ALEFT = [1,6] ARIGHT = [6,7], BLEFT = [1,2,4] , BRIGHT = [5,7,8]
* Not Valid Partion as MAX(ALEFT) > MIN(BRIGHT) --> We need to reduce elements in ALEFT --> R = MID -1 
* L = 0, R = 0
* MID = 0 
* ALEFT = [1] ARIGHT = [6,6,7], BLEFT = [1,2,4,5] , BRIGHT = [7,8]
* Valid Partition 
* return MEDIAN = MAX(1,5) + MIN(6,7) // 2 = 5+6//2 = 11


'''

# NOTE: In python2.x, there is an issue integer division. Use python3 
class Solution(object):
    
    def valid_left_value(self, idx, arr): 
        if idx>=0:
            return arr[idx]
        else:
            return float("-inf")
        
    def valid_right_value(self, idx, arr):
        if idx < len(arr):
            return arr[idx]
        else:
            return float("inf") 
    
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        
        
        A = nums1 if len(nums1) < len(nums2) else nums2
        B = nums2 if len(nums2) > len(nums1) else nums1 
        
        K = len(A)+len(B)
        
        L , R = 0 , len(A)-1 
        HALF = K//2 #How many elements on each side of MEDIAN 
        
        # Running Binary Search on the smaller array
        
        while True: 
            MID = L + (R-L)//2 
            
            #  what if the below indexes goes out of bounds for some reason 
            #  we will place -inf and +inf at left and right bounds of each array so that comparison can always work 
            MAX_ALEFT_IDX = MID
            MIN_ARIGHT_IDX = MID+1 
            ALEFT_ELEMENTS = MID + 1 # 1 added to adjust 0 based indexes 
            BLEFT_ELEMENTS = HALF - (ALEFT_ELEMENTS) 
            MAX_BLEFT_IDX = BLEFT_ELEMENTS-1 
            MIN_BRIGHT_IDX = BLEFT_ELEMENTS 
            
            # check if partition that we did , is correct as per 
            
            if self.valid_left_value(MAX_ALEFT_IDX, A) <= self.valid_right_value(MIN_BRIGHT_IDX, B) and self.valid_left_value(MAX_BLEFT_IDX, B) <= self.valid_right_value(MIN_ARIGHT_IDX, A):
                # valid partition 
                
                # if resultant array will odd length 
                if K%2==1:
                    return min(self.valid_right_value(MIN_ARIGHT_IDX, A),self.valid_right_value(MIN_BRIGHT_IDX, B) )
                else:
                    AA = min(self.valid_right_value(MIN_ARIGHT_IDX, A),self.valid_right_value(MIN_BRIGHT_IDX, B))
                    BB = max(self.valid_left_value(MAX_ALEFT_IDX, A), self.valid_left_value(MAX_BLEFT_IDX, B))
                    print("AA", AA)
                    print("BB", BB)
                             
                    return ( min(self.valid_right_value(MIN_ARIGHT_IDX, A),self.valid_right_value(MIN_BRIGHT_IDX, B) ) + max(self.valid_left_value(MAX_ALEFT_IDX, A), self.valid_left_value(MAX_BLEFT_IDX, B))) /2 
                
            elif self.valid_left_value(MAX_ALEFT_IDX, A) > self.valid_right_value(MIN_BRIGHT_IDX, B) : 
                R = MID -1 
            elif self.valid_left_value(MAX_BLEFT_IDX, B) > self.valid_right_value(MIN_ARIGHT_IDX, A):
                L = MID + 1 
                
            
          
nums1 = [1,2]
nums2 = [3,4]

obj = Solution()

print(obj.findMedianSortedArrays(nums1, nums2))
  
