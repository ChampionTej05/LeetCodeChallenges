'''
https://leetcode.com/problems/evaluate-reverse-polish-notation/
'''

import math
def is_operand(token):
    return token in ("-", "/", "*", "+")


def calculate(number1, number2, operand):
    
   if operand == "+": return number1 + number2 
   if operand == "-": return number1 - number2 
   if operand == "*": return number1 * number2 
   if operand == "/": 
      res = number1/number2
      if res>0: return math.floor(res)
      else: return math.ceil(res)

def reverse_polish_notation(tokens):

    stack = []

    for token in tokens:
        if is_operand(token):
            #calculate
            operand = token 
            number2 = stack.pop() 
            number1 = stack.pop()
            print("{} {} {}".format(number1, operand, number2))
            result = int(calculate(number1, number2, operand))
            stack.append(result)
        else:
            # numbers 
            stack.append(int(token))

    print(stack)
    return stack.pop()


tokens = ["2","1","+","3","*"]
# tokens = ["4","13","5","/","+"]
tokens = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
tokens = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
print(reverse_polish_notation(tokens))