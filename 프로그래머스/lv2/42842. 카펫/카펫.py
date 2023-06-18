def solution(brown, yellow):
    total = brown + yellow
    m = total // 2
    
    for h in range(3, m):
        for w in range(h, m):
            if h * w == total and (h - 2) * (w - 2) == yellow:
                return [w, h]
            if h * w > total:
                break
            
    
    