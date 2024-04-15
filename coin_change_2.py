'''
This is variant of coin change where we are given infinite denominations of each coin and 
we need to find out whether we can sum upto that AMOUNT or not 


Approach 1 :
Brute Force DFS :-
- We start with sum = 20 and explore each path with two conditions 
    - if sum > 0 and numberBeingExplored < sum :
        explore(number)

Algo: 
sort(coins, reverse=True)
stack = []
sum = amount
minCoins = inf
for idx in range(len(coins)):
    if sum > 0 and sum <= coins[idx]:
        sum = sum - coins[idx]
        coinsRequired = explore(coins, sum)
        minCoins = min(coinsRequired+1, minCoins)
    else:
        break
        
return minCoins


'''


#brute force approach 
def explore_coins(coins, amount):
    if amount == 0:
        return 0
    if amount < 0:
        return float("inf")
    print("Coins: {}, amount: {}". format(coins,amount))
    minCoins = float("inf")
    for idx in range(len(coins)):
        if amount >= coins[idx]:
            coinsRequired = explore_coins(coins, amount - coins[idx])
            print("CoinsRequired: {}".format(coinsRequired))
            minCoins = min(coinsRequired+1, minCoins) 
            

    return minCoins 


def explore_coins_optimised(coins, amount, memo):
    if amount < 0:
        return float("inf")
    if amount == 0:
        return 0        
    if amount in memo:
        return memo[amount]
    
    min_coins = float("inf")
    for idx in range(len(coins)):
        if amount >= coins[idx]:
            count = explore_coins_optimised(coins,  amount- coins[idx], memo )
            min_coins = min(min_coins, count+1)
    
    # answer for current amount would 
    memo[amount] = min_coins 
    return min_coins

def coinChange(coins, amount):
    coins.sort(reverse=True)
    # coinsRequired = explore_coins(coins, amount)

    coinsRequired = explore_coins_optimised(coins, amount, memo= {})
    minCoins = coinsRequired if coinsRequired!= float("inf") else -1 

    print(minCoins)

def dp_coin_change(coins,amount):
    ''''
    Neetcode: https://www.youtube.com/watch?v=H9bfqozjoqs 

    dp[amount] = 1 + min( dp[amount-coin] for coin in coins)
    where dp[0]= 0 

    We calculate how many required for each amount from 0 -- amount-1 and then 
    use that information to find the answer to the amount 


    '''
    
    dp = [amount+1] * (amount+1)

    dp[0] = 0

    for amt in range(1, amount+1):
        for coin in coins:
            if coin <= amt:
                print("Coin:{}, amount: {}".format(coin, amt))
                dp[amt] = min(dp[amt], 1+ dp[amt-coin])
                print("DP: ", dp)


    
    print(dp)
    return dp[amount] if dp[amount] != amount+1 else -1 


coins = [1,2,5]
amount = 11

# coins = [1,4,5,7,10,11,15,21]
# amount = 20

# coins = [186,419,83,408]
# amount = 6249
# coinChange(coins, amount)
dp_coin_change(coins, amount)