'''
3 Sum Number Problem : 
Take non-empty distinct array of integers and target sum. 
Find all triplets to target sum. 
Triplets should be in ascending order and should be sorted inside themselves too. 

ex: {
  "array": [12, 3, 1, 2, -6, 5, -8, 6],
  "targetSum": 0
}
o/p : [[8.2.6], [-8,3,5], [-6, 1 5 ]]

Questions
Algoexpert: https://www.algoexpert.io/questions/three-number-sum 
Leetcode: https://leetcode.com/problems/3sum/

Approach : Using 2Sum Problem 
time complexity: o(n*n) in time and o(n*3) in space
- Sort the Array (so that triplets can be in sorted order)
- Write 2-sum problem solution 
- Divide 3-sum problem into (N-1) 2-sum problems 

Sudo Code: 

def find3NumberSum(arr, target):
    arr.sort()
    results = list()
    for i in range(len(arr)):
        solutions_2sum = 2SumProblem(arr[i+1:], target-arr[i])
        for every sol in solutions:
            results.append([arr[i], sol[0], sol[1]])
    

'''

from custom_test_loader import CustomTestLoader
import unittest

def threeNumberSum(array, targetSum):
    #using two-pointer approach 

    array.sort()
    results = list()
    aset = set()

    for i in range(len(array)):
        #avoids duplicate  for first number
        if i>0 and array[i] == array[i-1]:
            continue
        target_sum_for_2Sum =  targetSum - array[i]

        left = i +1
        right = len(array)-1 
        while left < right:
            current_sum = array[left] + array[right ]
            if current_sum > target_sum_for_2Sum:
                right = right - 1
            elif current_sum < target_sum_for_2Sum :
                left = left + 1
            else:
                # we found the sum 
                # print("Sum Found")
                results.append([array[i], array[left], array[right]])
                # aset.add(tuple([array[i], array[left], array[right]]))


                # remove duplicates pointers, to keep the triplets unique 
                while left < right and (array[left+1] == array[left]):
                        left = left +1 

                while left < right and (array[right-1] == array[right]):
                    right = right - 1

                left = left +1 
                right = right -1 

    # print(results)

    # Filter out duplicate triplets
    unique_results = []
    seen = set()
    for triplet in results:
        triplet_tuple = tuple(triplet)
        if triplet_tuple not in seen:
            unique_results.append(triplet)
            seen.add(triplet_tuple)

    return unique_results
    # return list([list(a) for a in aset])
    # return results 


class TestThreeSum(unittest.TestCase):
    def __init__(self, methodName: str = "runTest", approach = 1) -> None:
        super().__init__(methodName)
        self.approach = approach

    
    def execute_approach(self, num, target):
        if self.approach ==1 :
            return threeNumberSum(num , target) 

    
    def test_basic(self):
        num = [12, 3, 1, 2, -6, 5, -8, 6]
        target = 0 
        expected_ans = [ [-8,2,6],[-8,3,5],[-6,1,5]]

        self.assertEqual(self.execute_approach(num, target), expected_ans)

    def test_case_empty_answer(self):
        num = [1, 2, 3]
        target = 7
        expected_ans = []

        self.assertEqual(self.execute_approach(num, target), expected_ans)

    def test_case_single_answer(self):
        
        num = [1, 2, 3]
        target = 6
        expected_ans = [[1,2,3]]

        self.assertEqual(self.execute_approach(num, target), expected_ans)

    def test_case_multi_answer(self):
        num = [1, 2, 3, 4, 5, 6, 7, 8, 9, 15]
        target = 18
        expected_ans = [
                    [1, 2, 15],
                    [1, 8, 9],
                    [2, 7, 9],
                    [3, 6, 9],
                    [3, 7, 8],
                    [4, 5, 9],
                    [4, 6, 8],
                    [5, 6, 7]
                    ]

        self.assertEqual(self.execute_approach(num, target), expected_ans)



if __name__ == "__main__":
    loader = CustomTestLoader()
    suite = loader.loadTestsFromTestCase(TestThreeSum, approach = 1)
    unittest.TextTestRunner().run(suite)
        

    