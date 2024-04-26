# # Recursive Approach
def max_profit(ind, buy, prices, n):

    if(ind >= n):
        return 0

    profit = 0

    if(buy == 1):
        profit = max( -prices[ind] + max_profit(ind+1, 0, prices, n), 
                     0 + max_profit(ind+1, 1, prices, n) )
    else:
        profit = max(prices[ind] + max_profit(ind+1, 1, prices,n), 
                     0 + max_profit(ind+1, 0, prices, n))
        
    return profit


# # Memoization Approach 
# TC - O(N*2)
# SC - O(N*2) + O(N)
def max_profit(ind, buy, prices, n, dp):
    
    if(ind >= n):
        return 0

    if(dp[ind][buy] != -1):
        return dp[ind][buy]

    profit = 0

    if(buy == 1):
        profit = max( -prices[ind] + max_profit(ind+1, 0, prices, n, dp), 
                     0 + max_profit(ind+1, 1, prices, n, dp) )
    else:
        profit = max(prices[ind] + max_profit(ind+1, 1, prices,n, dp), 
                     0 + max_profit(ind+1, 0, prices, n, dp))
        
    dp[ind][buy] = profit
    return profit



# # Tabulation Approach

def max_profit(prices):

    n = len(prices)

    dp = [[-1] * 2 for _ in range(n)] 

    dp[n][1] = 0
    dp[n][0] = 0

    

    # for i in range(start, stop , step)

    for i in range(n-1, -1, -1):
        profit = 0
        for buy in range(0, 2):
            
            if(buy == 1):
                dp[i][buy] = max( -prices[i] + dp[i+1][0], 
                                 0 + dp[i+1][1] )
            else:
                dp[i][buy] = max(prices[i] + dp[i+1][1], 
                                 0 + dp[i+1][0])
            
            dp[i][buy] = profit

    return dp[0][1]


# # Remove Auxiliary Space

def max_profit_ii(prices):
    
    n = len(prices)

    ahead = [-1] * 2
    curr = [-1] * 2

    ahead[1] = 0
    ahead[0] = 0

    profit = 0

    # for i in range(start, stop , step)

    for i in range(n-1, -1, -1):
        profit = 0
        for buy in range(0, 2):
            if(buy == 1):
                profit = max(-prices[i] + ahead[0], 0 + ahead[1])
            else:
                profit = max(prices[i] + ahead[1], 0 + ahead[0])
            
            
            curr[buy] = profit
        
        ahead = curr


    return ahead[1]

    

# ---------------------------------------------------------------------------
prices = [7,1,5,3,6,4]
n = len(prices)
print(max_profit(0, 1, prices, n))