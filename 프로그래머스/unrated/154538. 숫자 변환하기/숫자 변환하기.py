def solution(x, y, n):
    dp = [1_000_001] * (y+1)
    dp[x] = 0
    
    for i in range(x+1, y+1):
        if i - n >= 0:
            dp[i] = dp[i-n] + 1
        if not i % 2:
            dp[i] = min(dp[i], dp[i//2]+1)
        if not i % 3:
            dp[i] = min(dp[i], dp[i//3]+1)
    
    return -1 if dp[y] > 1_000_000 else dp[y]