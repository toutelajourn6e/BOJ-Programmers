def possible(mid, stones, k):
    cnt = 0
    for stone in stones:
        if mid > stone:
            cnt += 1
            if cnt >= k:
                return False
        else:
            cnt = 0
    return True

def solution(stones, k):
    start, end = 0, max(stones)
    ans = 0
    
    while start <= end:
        mid = (start + end) // 2
        if possible(mid, stones, k):
            ans = max(ans, mid)
            start = mid + 1
        else:
            end = mid - 1
            
    return ans
            
    