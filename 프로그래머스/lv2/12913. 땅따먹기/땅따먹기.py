def solution(land):
    n = len(land)
    dp = [[0] * 4 for _ in range(n)]
    
    for i in range(n):
        if not i:
            for j in range(4):
                dp[i][j] = land[i][j]
        dp[i][0] = max(dp[i-1][1], dp[i-1][2], dp[i-1][3]) + land[i][0]
        dp[i][1] = max(dp[i-1][0], dp[i-1][2], dp[i-1][3]) + land[i][1]
        dp[i][2] = max(dp[i-1][0], dp[i-1][1], dp[i-1][3]) + land[i][2]
        dp[i][3] = max(dp[i-1][0], dp[i-1][1], dp[i-1][2]) + land[i][3]
        
    return max(dp[n-1])
        