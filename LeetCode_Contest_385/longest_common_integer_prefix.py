'''
https://leetcode.com/contest/weekly-contest-385/problems/find-the-length-of-the-longest-common-prefix/

Solution present in leetcode 
'''


class Solution(object):
    
    def common_prefix_of_integers(self,num1, num2):
        
        if num1 == num2:
            return len(str(num1))
        
        count =0 
        
        while num1>0 and num2>0:
            if num1==num2:
                count = len(str(num1))
                break
            if num1>num2:
                num1//=10
            elif num2>num1:
                num2//=10 
                
        return count
                
    
    def longestCommonPrefix(self, arr1, arr2):
        """
        :type arr1: List[int]
        :type arr2: List[int]
        :rtype: int
        """
        arr1.sort(reverse=True)
        arr2.sort(reverse=True)
        max_prefix_length = 0 
        for i in range(len(arr1)):
            for j in range(len(arr2)):
                
                prefix_length = self.common_prefix_of_integers(arr1[i], arr2[j])
                print(arr1[i], arr2[j],prefix_length)
                
                max_prefix_length = max(max_prefix_length, prefix_length)
        return max_prefix_length
    
obj = Solution()

arr1= [13,27,45]
arr2 = [21,27,48]

arr1 = [123, 4567, 89]
arr2 = [1234, 567, 890]

arr1 = [2161,7400,4662]
arr2 = [7542,7483,8628,3345]

print(obj.longestCommonPrefix(arr1, arr2))
        