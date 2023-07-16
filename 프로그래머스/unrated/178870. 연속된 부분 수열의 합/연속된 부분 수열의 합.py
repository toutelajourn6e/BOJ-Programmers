def solution(sequence, k):
    n = len(sequence)
    ans = [0, n-1]
    left, right = 0, 0
    interval = sequence[right]
    
    while left <= right and right < n:
        if interval == k:
            if left == right: return [left, right]
            elif right - left < ans[1] - ans[0]:
                ans = [left, right]
                right += 1
                if right == n: break 
                interval += sequence[right]
        if interval > k:
            interval -= sequence[left]
            left += 1
            continue
        right += 1
        if right == n: break
        interval += sequence[right]
        
    return ans