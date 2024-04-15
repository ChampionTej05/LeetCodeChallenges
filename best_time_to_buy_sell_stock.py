def maxProfitBruteForce( prices):
    #maximise profit 

    #brute force 

    global_max = 0 
    for i in range(len(prices)-1):
        for j in range(i,len(prices)):
            profit = prices[j]- prices[i]
            if profit > global_max:
                global_max = profit 

    print("Profit Returned : ", global_max)
    return global_max  

def maxProfit(prices):
    '''
    Logic: 
    - start from end 
    - we find difference between buy and sell and check if we get bigger number than current sell using buy ptr
    - if we find, then we set , sellptr to that number as it might  increase profit 
    - else we just keep finding max_profit 
    '''
    if len(prices) <2:
        return 0 
    buyPtr = len(prices)-2
    sellPtr = len(prices)-1
    max_profit = 0

    while buyPtr>=0:
        if prices[sellPtr] > prices[buyPtr]:
            max_profit = max(prices[sellPtr]-prices[buyPtr], max_profit)
        else:
            sellPtr = buyPtr
        buyPtr = buyPtr-1 

    return max_profit
    
def test_maxProfit():
    # Test case 1: Example with increasing prices
    prices1 = [1, 2, 3, 4, 5]
    result1 = maxProfit(prices1)
    assert result1 == 4  # Buy at 1, sell at 5 for a profit of 4

    # Test case 2: Example with decreasing prices
    prices2 = [5, 4, 3, 2, 1]
    result2 = maxProfit(prices2)
    assert result2 == 0  # No profit can be made

    # Test case 3: Random prices
    prices3 = [7, 1, 5, 3, 6, 4]
    result3 = maxProfit(prices3)
    assert result3 == 5  # Buy at 1, sell at 6 for a profit of 5

    # Test case 4: Empty list
    prices4 = []
    result4 = maxProfit(prices4)
    assert result4 == 0  # No profit can be made with an empty list


    prices5 = [3, 5, 2, 9, 7, 6] 
    result5 =maxProfit(prices5)
    assert result5 == 7


    prices9 = [10, 5, 8, 3, 7, 11, 9, 2, 12]
    result9 = maxProfit(prices9)
    assert result9 == 10


    print("All test cases passed!")

# Run the test function
test_maxProfit()
# prices2 = [5, 4, 3, 2, 1]
# result2 = maxProfit(prices2)
# print(result2)