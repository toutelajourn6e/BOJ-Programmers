import heapq as hq

def solution(food_times, k):
    if sum(food_times) <= k:
        return -1
    
    n = len(food_times)
    pq = []
    for i in range(n):
        hq.heappush(pq, (food_times[i], i+1))
        
    spend = 0
    pre = 0
    length = n
    
    while spend + ((pq[0][0] - pre) * length) <= k:
        cur = hq.heappop(pq)[0]
        spend += (cur - pre) * length
        length -= 1
        pre = cur
        
    result = sorted(pq, key = lambda x: x[1])
    
    return result[(k - spend) % length][1]