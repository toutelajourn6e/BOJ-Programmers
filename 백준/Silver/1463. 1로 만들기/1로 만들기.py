n = int(input())

dp = [0]*(n+1)
dp[1] = 0

for num in range(2, n+1):
    dp[num] = dp[num - 1] + 1
    if num % 2 == 0 and dp[num] > dp[num//2] + 1:
        dp[num] = dp[num//2] + 1
    if num % 3 == 0 and dp[num] > dp[num//3] + 1:
        dp[num] = dp[num//3] + 1
    
print(dp[n])