def coin_change(coins, amount):
    '''
    Parameters:
            Takes in a list of integers and a summed amount
    Returns:
            Outputs the minimum number of coin flips needed to achieve summed amount
    '''
    # Solution done using backtracking brute force DP algorithm
    dp = [amount + 1] * (amount + 1)
    dp[0] = 0  # base case if there are 0 coins being used, then return 0

    for a in range(1, amount+1):  # go upto the amount of coins being used
        for c in coins:  # compute the coins being used
            if a - c >= 0:  # Keep searching if the summed amount has not been reached yet
                # store the minimum of the number of coins being used
                dp[a] = min(dp[a], 1 + dp[a-c])

    # Last edge case if there is no number of coin flips that can sum the amount given
    # Otherwise just returns -1
    return dp[amount] if dp[amount] != amount + 1 else -1


# Testing
# Expected output: 3
coins = [1, 2, 5]
amount = 11
print(coin_change(coins, amount))
