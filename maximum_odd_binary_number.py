'''
https://leetcode.com/problems/maximum-odd-binary-number/?envType=daily-question&envId=2024-03-01
'''

class Solution(object):
    
    def usingStringConcat(self, s):
        one_count = s.count('1')

        new_string = '1'*(one_count-1) + '0'*(len(s)-one_count) + '1'
        return new_string

    def usingTwoPointer(self, s):
        binary_list = list(s)
        left, right = 0, len(binary_list) - 1
        first_one_to_end_swapped = False

        while left <= right:
            if binary_list[left] == '0' and binary_list[right] == '1':
                if not first_one_to_end_swapped:
                    binary_list[right], binary_list[-1] = binary_list[-1], binary_list[right]
                    first_one_to_end_swapped = True
                    right -= 1
                else:
                    binary_list[left], binary_list[right] = binary_list[right], binary_list[left]
                    left += 1
                    right -= 1
            else:
                if binary_list[left] == '1':
                    left += 1
                if binary_list[right] == '0':
                    right -= 1

        if not first_one_to_end_swapped:
            binary_list[left - 1], binary_list[-1] = binary_list[-1], binary_list[left - 1]

        return ''.join(binary_list)


    def maximumOddBinaryNumber(self, s):
        """
        :type s: str
        :rtype: str
        """
        
        return self.usingTwoPointer(s)

        
        
s = "010"
s= "0101"
s = "10100100"
s = "000001"
obj = Solution()
obj.maximumOddBinaryNumber(s)
