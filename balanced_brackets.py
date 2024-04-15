class Stack:

    def __init__(self) -> None:
        self.stack = []

    def push(self, value): 
        self.stack.append(value)

    def pop(self) -> object:
        if not self.is_empty():
            return self.stack.pop()
        else:
            return None

    def is_empty(self) -> bool:
        return len(self.stack) == 0
    

'''
Algo 
1. If we see anything from closing brakcet, push onto stack 
2. If we see anythign from opening brakcet, pop from stack and check if it has it's comparable or not 


How to find comparable?
Create mapper {"closing_bracket": "opening_bracket"}
'''

def balancedBrackets(string):
    stack = Stack()
    mapper = {
        ")": "(",
        "}": "{",
        "]": "["
    }

    for chr in reversed(string):
        if chr in mapper.keys():
            stack.push(chr)
        elif chr in mapper.values():
            popped_chr = stack.pop()
            
            if not popped_chr or chr != mapper[popped_chr]:
                return False 
            
    return  stack.is_empty() 



s = "([])(){(())()()"

print(balancedBrackets(s))

