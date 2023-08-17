def solution(sticker):
    if len(sticker) == 1: return sticker[0]
    n = len(sticker)
    dp1 = [0] * n
    dp2 = [0] * n

    for i in range(n-1):
        dp1[i] = max(dp1[i-2] + sticker[i], dp1[i-1])
        
    for i in range(1, n):
        dp2[i] = max(dp2[i-2] + sticker[i], dp2[i-1])
        
    return max(max(dp1), max(dp2))