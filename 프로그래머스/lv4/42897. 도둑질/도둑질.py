def solution(money):
    n = len(money)
    dp1, dp2 = [0] * n, [0] * n
    dp1[0] = money[0]; dp1[1] = money[1]
    dp2[1] = money[1]
    
    for i in range(n-1):
        dp1[i] = max(dp1[i-2] + money[i], dp1[i-1])
        
    for i in range(1, n):
        dp2[i] = max(dp2[i-2] + money[i], dp2[i-1])
        
    
    return max(max(dp1), max(dp2))