
class MyQueue(object):

    def __init__(self):

        self.enque = []
        self.deque = []
        

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """

        if not self.enque : 
            while self.deque:
                self.enque.append(self.deque.pop())
        self.enque.append(x)
        

    def pop(self):
        """
        :rtype: int
        """

        if not self.deque:
            while self.enque:
                self.deque.append(self.enque.pop())
        return self.deque.pop() if self.deque else None
        

    def peek(self):
        """
        :rtype: int
        """
        
        if not self.deque:
            while self.enque:
                self.deque.append(self.enque.pop())
        return self.deque[-1] if self.deque else None
        

    def empty(self):
        """
        :rtype: bool
        """

        return [] == (self.enque or self.deque)
    

obj = MyQueue()

obj.push(12)
obj.push(14)
obj.push(90)
param_2 = obj.pop()
param_3 = obj.peek()
param_4 = obj.empty()

print(param_2, param_3, param_4)

obj.push(45)
obj.pop()
obj.push(32)
obj.pop()
print(obj.enque)
print(obj.deque)
        