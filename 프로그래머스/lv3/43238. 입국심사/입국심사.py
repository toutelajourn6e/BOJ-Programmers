def solution(n, times):
    ans = 0
    start, end = 1, max(times) * n
    
    while start <= end:
        mid = (start + end) // 2
        people = 0
        
        for time in times:
            people += mid // time
            if people >= n:
                break
                
        if people >= n:
            ans = mid
            end = mid - 1
            
        elif people < n:
            start = mid + 1
            
    return ans
        