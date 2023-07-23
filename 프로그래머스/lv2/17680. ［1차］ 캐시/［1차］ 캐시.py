from collections import deque

def solution(cacheSize, cities):
    if not cacheSize: return len(cities) * 5
    ans = 0
    cache = deque()
    
    for city in cities:
        city = city.upper()
        if not cache:
            ans += 5
            cache.append(city)
        elif cache and city not in cache:
            ans += 5
            cache.append(city)
        else:
            ans += 1
            cache.remove(city)
            cache.append(city)
        if len(cache)-1 == cacheSize: cache.popleft()
    
    return ans