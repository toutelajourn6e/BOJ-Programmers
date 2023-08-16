def solution(n, stations, w):
    ans = 0
    distance = []
    
    for i in range(1, len(stations)):
        distance.append((stations[i] - w - 1) - (stations[i-1] + w))
        
    distance.append(stations[0] - w - 1)
    distance.append(n - (stations[-1] + w))
    
    for d in distance:
        if d > 0:
            q, r = divmod(d, (2 * w + 1))
            ans += q
            if r: ans += 1
            
    return ans