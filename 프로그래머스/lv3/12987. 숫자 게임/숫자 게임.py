import heapq as hq

def solution(A, B):
    ans = 0
    hq.heapify(A)
    hq.heapify(B)
    
    for _ in range(len(A)):
        if not B: break
        a = hq.heappop(A)
        while B:
            b = hq.heappop(B)
            if b > a: 
                ans += 1
                break
    return ans