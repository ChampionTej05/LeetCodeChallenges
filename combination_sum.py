'''
https://leetcode.com/problems/combination-sum/

We will try brute force dfs approach to solve this problem and then may be use DP if possible to build up the solution
'''


def combination_sum_brute_force(candidates, target, answer, result, start):
    # Base condition: if target is zero, append the current combination to result
    if target == 0:
        result.append(answer.copy())
        return
    
    for i in range(start, len(candidates)):
        candidate = candidates[i]
        if candidate <= target:
            # Add the candidate to the current combination
            answer.append(candidate)
            # Recur with reduced target
            combination_sum_brute_force(candidates, target - candidate, answer, result, i)
            # Backtrack: remove the last element before the next iteration
            answer.pop()



def combination_sum_recursive(candidates, target, current_answer, results, start):
    
    if start == len(candidates):
        if target == 0:
            results.append(current_answer.copy())
        return
        
    
    #add the current element and recur 
    
    if (candidates[start] <= target):
        #element can be added 
        current_answer.append(candidates[start])
        combination_sum_recursive(candidates, target-candidates[start], current_answer, results, start)
        #once done, we need to pop the added element , so that backtracking can add next element 
        current_answer.pop()
        
    # add next element 
    combination_sum_recursive(candidates, target, current_answer, results, start+1)

candidates = [2,3,6,7]
target = 7   


candidates.sort(reverse=False)
result = []
start = 0
combination_sum_brute_force(candidates, target, [] , result, start)
print(result)

result = []
start = 0
combination_sum_recursive(candidates, target, [] , result, start)
print(result)