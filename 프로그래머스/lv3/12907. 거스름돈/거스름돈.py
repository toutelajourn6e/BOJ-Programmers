def solution(n, money):
    dp = [0] * (n + 1)
    dp[0] = 1
    
    
    for i in range(len(money)):
        for j in range(1, n + 1):
            if j - money[i] >= 0:
                dp[j] += dp[j-money[i]]
    
    return dp[n]