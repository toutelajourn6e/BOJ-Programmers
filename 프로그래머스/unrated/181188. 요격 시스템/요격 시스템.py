def solution(targets):
    targets.sort(key=lambda x: x[1])
    point, ans = -1, 0
    
    for s, e in targets:
        if s >= point:
            point = e
            ans += 1
    return ans