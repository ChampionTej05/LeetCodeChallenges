'''
https://leetcode.com/problems/find-numbers-with-even-number-of-digits/ 

Find how many numbers have even digits in the array 

'''

'''
Solution :

Approach 1 : Count no of digits using while loop, if even then increment count O(n*n)
Approach 2: Convert each no into string and check if the length of string is even or not O(n*n)
Approach 3: Use math.log.base10 to count no of digits effficiently O(n*logn)
'''

import unittest
import math
from custom_test_loader import CustomTestLoader

def findNumbersApproach1(nums)-> int:
    count = 0
    for num in nums:
        num_digits = v1_get_digits(num)
        count = count+1 if num_digits %2 == 0 else count
    return count

def v1_get_digits(num):
    if num==0:
        return 1
    num = num*-1 if num<0 else num
    digit_count = 0 
    while num>0:
        digit_count = digit_count+1
        num= num//10 
    return digit_count

def findNumbersApproach2(nums) -> int:
    count = 0
    for num in nums:
        num_digits = v2_get_digits(num)
        print(num, num_digits)
        count = count+1 if num_digits %2 == 0 else count
    return count

def v2_get_digits(num):
    if num == 0:
        return 1  # Zero has one digit
    num = abs(num)  # Handle negative numbers
    digit_count = int(math.log10(num)) + 1  # Correct number of digits for positive numbers
    return digit_count

def findNumbersApproach3(nums):

    count =0 
    for num in nums:
        if len(str(abs(num))) % 2 == 0:
            count+=1
    return count


# class CustomTestLoader(unittest.TestLoader):
#     def loadTestsFromTestCase(self, testCaseClass, approach=1):
#         if issubclass(testCaseClass, unittest.suite.TestSuite):
#             raise TypeError("Test cases should not be derived from TestSuite. Maybe you meant to derive from TestCase?")
#         testCaseNames = self.getTestCaseNames(testCaseClass)
#         testCases = []
#         for name in testCaseNames:
#             testCases.append(testCaseClass(name, approach=approach))
#         loaded_suite = self.suiteClass(testCases)
#         return loaded_suite

class TestEvenDigitsInArray(unittest.TestCase):
    def __init__(self, methodName: str = "runTest", approach=1 ) -> None:
        super().__init__(methodName)
        self.approach = approach 

    def execute_approach(self, nums):
        # print("self.approach", self.approach)
        if self.approach == 1:
            return findNumbersApproach1(nums)
        elif self.approach == 2:
            return findNumbersApproach2(nums)
        elif self.approach == 3:
            return findNumbersApproach3(nums)
        
    def test_basic(self):
        nums = [12,345,2,6,7896]
        self.assertEqual(self.execute_approach(nums), 2)

    def test_negative_numbers(self):
        nums = [-1,22,90,-12, 666]
        self.assertEqual(self.execute_approach(nums), 3)
    
    def test_zero_number(self):
        nums = [0, 1]
        self.assertEqual(self.execute_approach(nums), 0)
        


if __name__ == '__main__':
    loader = CustomTestLoader()
    suite1 = loader.loadTestsFromTestCase(TestEvenDigitsInArray, approach=3)
    unittest.TextTestRunner().run(suite1)

    # nums = [12,345,2,6,7896]
    # print(findNumbersApproach2(nums))





