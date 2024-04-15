def nonConstructibleChange(coins):
    # Write your code here.
    if len(coins) == 0:
        return 1 
    
    coins.sort()

    sum_till_now =0

    for coin in coins:
        
        if coin <= sum_till_now +1:
            sum_till_now = sum_till_now + coin 
        else:
            break
        
    return sum_till_now + 1 


def test_nonConstructibleChange():
    # Test case 1: Example with a single coin
    coins1 = [1]
    result1 = nonConstructibleChange(coins1)
    assert result1 == 2  # The minimum non-constructible change is 2.

    # Test case 2: Example with multiple coins
    coins2 = [1, 2, 5]
    result2 = nonConstructibleChange(coins2)
    assert result2 == 4  # The minimum non-constructible change is 4.

    # Test case 3: Example with coins that can create all possible change
    coins3 = [1, 2, 3, 4, 5]
    result3 = nonConstructibleChange(coins3)
    assert result3 == 16  # All values from 1 to 16 can be created.

    # Test case 4: Example with coins that have gaps in possible change
    coins4 = [1, 2, 4, 8]
    result4 = nonConstructibleChange(coins4)
    print(result4)
    assert result4 == 16  # The minimum non-constructible change is 16.

    # Test case 5: Example with no coins
    coins5 = []
    result5 = nonConstructibleChange(coins5)
    assert result5 == 1  # The minimum non-constructible change is 1.

    print("All test cases passed!")

# Run the test function
test_nonConstructibleChange()
