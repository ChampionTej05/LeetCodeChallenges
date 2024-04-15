
'''
Valid parenthesis 
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

ex: s = "({{[]([])}})"
o/p : True 

ex: s = ""
o/p : True 


Approach : using stack 
time complexity : O(n) in time and space

Code:
def validate_parenthesis(string):

    stack=[]
    for i in range(len(arr)-1, -1):
        if isClosingBracket(arr[i]) :
            stack.push(arr[i])
        elif:
            if matchedOpening(stack.peek(), arr[i]):
                stack.pop()
            else: 
                return false 

    if stack.len==0:
        return true 
    else:
        return false 
'''
import unittest
from custom_test_loader import CustomTestLoader
def is_closing_brace(ch):
    return ch in [']', '}', ')']

def is_matching_brace(openingBrace, closingBrace):
    if openingBrace == '(':
        if closingBrace == ')':
            return True 
    if openingBrace == "[":
        if closingBrace == "]":
            return True 
    if openingBrace == "{":
        if closingBrace == "}":
            return True 
        
    return False
        

    

def isValid(s):
    stack = []
    for i in range(len(s)-1, -1, -1):
        if is_closing_brace(s[i]):
            stack.append(s[i])
        else:
            if len(stack)> 0 and is_matching_brace(s[i], stack[-1]):
                stack.pop()
            else:
                return False
    return len(stack) == 0 


class TestValidParenthesis(unittest.TestCase):
    def __init__(self, methodName: str = "runTest", approach =1) -> None:
        super().__init__(methodName)
        self.approach = approach 

    
    def execute_approach(self, s):
        if self.approach == 1:
            return isValid(s)
        
    
    def test_basic(self):
        s = "()[]{}"
        expected_output = True 
        self.assertEqual(self.execute_approach(s), expected_output)

    def test_complex(self):
        s = "({{[]([])}})"
        expected_output = True 
        self.assertEqual(self.execute_approach(s), expected_output)

    def test_empty_string(self):
        s = ""
        expected_output = True 
        self.assertEqual(self.execute_approach(s), expected_output)

    def test_negative_case(self):
        s = "({{[([])})"
        expected_output = False 
        self.assertEqual(self.execute_approach(s), expected_output)

    

if __name__ == "__main__":
    loader = CustomTestLoader()
    suite = loader.loadTestsFromTestCase(TestValidParenthesis, approach=1)
    unittest.TextTestRunner().run(suite)