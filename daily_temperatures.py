'''
https://leetcode.com/problems/daily-temperatures/description/?envType=daily-question&envId=2024-01-31
'''



'''
Idea is to use stack to keep track temperatures waiting for seeing warmer in future 

answer = [0 for i in range(len(temperatures))]
For each temperature 
1. While stack is not empty & temperature > stack.top.temperature :
    temp_index = stack.pop.index
    answer[temp_index]= temperature.index - temp_index 
2. Push new warmer temperature on stack : stack.push(temperature.index)

ex: [73, 74, 75, 71, 69, 72, 76, 73]

'''

    

def daily_temperatures(temperatures):
    from collections import deque
    answers = [0 for i in range(len(temperatures))]
    remeberance_stack = deque()
    for i in range(len(temperatures)):

        current_temperature = temperatures[i]
        # pop for each index in stack, who are looking for warmer temperatures in future 
        while remeberance_stack and temperatures[remeberance_stack[-1]] < current_temperature:
            temp_index = remeberance_stack.pop()
            answers[temp_index] = i - temp_index

        # push temperature index for future comparison 
        remeberance_stack.append(i)

    return answers




temperatures =  [73, 74, 75, 71, 69, 72, 76, 73]

print(daily_temperatures(temperatures))