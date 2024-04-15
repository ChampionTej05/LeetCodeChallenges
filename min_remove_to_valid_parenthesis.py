'''
https://leetcode.com/problems/minimum-remove-to-make-valid-parentheses


Find the balanced parenthesis for each open parenthesis 

1. From left to right, if the ( is seen, push onto stack (,i
2. If ) is seen,
    - pop from stack if the stack is not empty --> balanced ( found for ) 
    - else replace index of ) with "" by marking that, no ( found for ) 
    
3. All the remaining ( in stack, doesn't have any ), so mark all the indexes for them = ""
'''


class Solution(object):
    def minRemoveToMakeValid(self, s):
        """
        :type s: str
        :rtype: str

        
        """
        
        stack = [] # stores the index of open parenthesis ( 
        
        alist = list(s)
        
        for idx, chr in enumerate(alist):
            
            if chr == '(':
                stack.append(idx)
            elif chr == ")":
                if len(stack) ==0:
                    alist[idx] = ""
                else:
                    stack.pop()
        
        
        print("Stack : ", stack)
        
        while len(stack)!=0:
            alist[stack.pop()] = ""
            
        return "".join(alist)
    
    
obj = Solution()

s = "lee(t(c)o)de)"

print(obj.minRemoveToMakeValid(s))
        