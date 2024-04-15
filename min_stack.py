'''
https://leetcode.com/problems/min-stack/

Push: Update minValue element everytime during push 

Pop: 
1. If the popped key is not minValue element, no issues
2. If the popped key is minValue element, how to get the next min value element 
    a. We can use auxiliary Stack to keep only minium elements 
    b. PUSH(key) will put element into AUX only if the key <= minValue
    c. POP() will check if popped key == top(AUX)
        a. If yes, then pop from AUX too 
        b. If no, then keep the AUX intact
'''

class MinStack(object):
    
    def __init__(self):

        
        self.stack = []
        self.min_stack = []

    def push(self, val):
        """
        :type val: int
        :rtype: None
        """
        
        self.stack.append(val)
        
        if not self.min_stack or val <= self.min_stack[-1]:
            self.min_stack.append(val)


    def pop(self):
        """
        :rtype: None
        """

        if self.stack:
            popped_key = self.stack.pop()
            print("Popped Key: ", popped_key)
            if popped_key != self.min_stack[-1]:
                return 
            min_value = self.min_stack.pop()


    def top(self):
        """
        :rtype: int
        """
        if self.stack:
            return self.stack[-1]
        

    def getMin(self):
        """
        :rtype: int
        """

        if self.min_stack:
            return self.min_stack[-1]
        


# Your MinStack object will be instantiated and called as such:
obj = MinStack()
for val in [4,3,2,5,1]:
    obj.push(val)
obj.pop()
param_3 = obj.top()
param_4 = obj.getMin()
print(param_3, param_4)