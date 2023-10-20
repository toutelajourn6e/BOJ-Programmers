import heapq as hq

def solution(scoville, K):
    hq.heapify(scoville)
    
    result = 0
    
    while len(scoville) > 1:
        min_v = hq.heappop(scoville)
        if min_v >= K:
            return result
        sec_v = hq.heappop(scoville)
        if sec_v == 0:
            return -1
        hq.heappush(scoville, min_v + (sec_v * 2))
        result += 1
        
    if scoville[0] >= K:
        return result
    else:
        return -1