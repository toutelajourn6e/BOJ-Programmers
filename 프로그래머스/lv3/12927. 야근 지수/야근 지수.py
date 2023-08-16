import heapq as hq

def solution(n, works):
    if sum(works) <= n: return 0
    pq = []
    for work in works:
        hq.heappush(pq, -work)
    hq.heapify(works)
    
    while n:
        work = hq.heappop(pq)
        hq.heappush(pq, work + 1)
        n -= 1
        
    ans = 0
    for elem in pq:
        ans += elem ** 2
    
    return ans