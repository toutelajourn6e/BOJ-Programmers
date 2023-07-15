def solution(n, k, enemy):
    if k >= len(enemy): return len(enemy)
    ans = 0
    start, end = 0, len(enemy)
    
    while start <= end:
        mid = (start + end) // 2
        round = sorted(enemy[:mid+1], reverse=True)
        if sum(round[k:]) <= n:
            ans = max(ans, mid)
            start = mid + 1
        else:
            end = mid - 1
    
    return len(enemy) if ans == len(enemy) else ans + 1
    
        
        