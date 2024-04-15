'''
Find Missing Number : https://leetcode.com/problems/missing-number/description/
Short Description: Given numbers in range [0,N], find missing number in array
'''

'''
Solution Approach 
1. Find the sum of all N whole numbers and find sum of all numbers in array. Missing number would be difference between both sums
2. Cyclic sort Algo, O(n): Place each number at its correct place in the array i.e. if nums[i]!=i , place nums[i] at nums[nums[i]] location.
    Check which number is not at correct after this process 
'''

import unittest
from custom_test_loader import CustomTestLoader



def findMissingNumberApproach1(nums):
    # Implement Approach 1: Sum of all numbers up to N minus sum of array
    n = len(nums)
    expected_sum = n * (n + 1) // 2
    actual_sum = sum(nums)
    return expected_sum - actual_sum

def findMissingNumberApproach2(nums):
    # Implement Approach 2: Cyclic Sort Algorithm
    i = 0
    n = len(nums)
    while i < n:
        if nums[i] < n and nums[i] != i:
            correct_index = nums[i]
            nums[i], nums[correct_index] = nums[correct_index], nums[i]
        else:
            i += 1

    for i in range(n):
        if nums[i] != i:
            return i

    return n



class TestMissingNumber(unittest.TestCase):
    def executeApproach(self, nums):
        if self.approach == 1:
            return findMissingNumberApproach1(nums)
        elif self.approach == 2:
            return findMissingNumberApproach2(nums)
        else:
            raise ValueError("Invalid approach")

    def __init__(self, methodName='runTest', approach=1):
            super().__init__(methodName)
            self.approach = approach

    def test_basic(self):
        self.assertEqual(self.executeApproach([3, 0, 1]), 2)

    def test_no_missing(self):
        self.assertEqual(self.executeApproach([0, 1, 2, 3]), 4)

    def test_missing_at_beginning(self):
        self.assertEqual(self.executeApproach([1, 2, 3, 4, 5]), 0)

    def test_missing_at_end(self):
        self.assertEqual(self.executeApproach([0, 1, 2, 3, 4]), 5)

    # def test_large_input(self):
    #     self.assertEqual(self.executeApproach(list(range(999, -1, -1))), 1000)

    def test_empty_input(self):
        self.assertEqual(self.executeApproach([]), 0)

    def test_complex_case(self):
        self.assertEqual(self.executeApproach([9,6,4,2,3,5,7,0,1]), 8)

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
    
if __name__ == '__main__':
    loader1 = CustomTestLoader()
    suite1 = loader1.loadTestsFromTestCase(TestMissingNumber, approach=1)
    unittest.TextTestRunner().run(suite1)

    loader2 = CustomTestLoader()
    suite1 = loader2.loadTestsFromTestCase(TestMissingNumber, approach=2)
    unittest.TextTestRunner().run(suite1)




