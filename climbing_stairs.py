'''
You are climbing a staircase. It takes n steps to reach the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?
https://leetcode.com/problems/climbing-stairs/

Approach : Using dynamic programming

Base case:
n = 0, return 0 
n =1 return 1 
n=2 return 2
ways(n) = ways(n-1) + ways(n-2), because you could come to N using n-1 th step and 1 or n-2 and 2 . Only two possible ways
'''

def climbStairsRecursive(n, mem):
    if n<=2:
        return mem[n] 
    if mem[n] !=0:
        return mem[n]
    mem[n]= climbStairsRecursive(n-1, mem) + climbStairsRecursive(n-2, mem)
    return mem[n]


def climbStairs(n):
    mem = [0]*(n+1)
    
    mem[0] = 0
    mem[1] = 1
    mem[2]= 2
    return climbStairsIterative(n, mem)


def climbStairsIterative(n, mem):

    for i in range(3, n+1):
        mem[i]= mem[i-1] + mem[i-2]
    return mem[n]
    


n = 45 
print(climbStairs(n))