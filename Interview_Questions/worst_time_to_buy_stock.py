'''
https://prepinsta.com/goldman-sachs/technical-test/coding-questions/

Prices=[10,4,2,9]
Ans = 8 (Buy at 10 and sell at 2 )
'''

def maxLoss(prices):
    if len(prices) < 2: 
        return 0 
    
    buyPtr = len(prices) - 2
    sellPtr = len(prices) - 1 

    maxLoss = 0

    while buyPtr >=0:
        if prices[sellPtr] < prices[buyPtr]:
            #we hit the loss   
            maxLoss = max(maxLoss, prices[buyPtr]-prices[sellPtr])

        else:
            sellPtr = buyPtr

        buyPtr = buyPtr-1

    return maxLoss

prices = [10, 4, 2, 9]
print(maxLoss(prices))