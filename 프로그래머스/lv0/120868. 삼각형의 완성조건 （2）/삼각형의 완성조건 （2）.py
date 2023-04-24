def solution(sides):
    long = max(sides)
    ans = 0
    
    for i in range(1, long * 2):
        if max(max(sides), i) == i:
            if i < sum(sides):
                ans += 1
        else:
            if max(sides) < min(sides) + i:
                ans += 1
        
    return ans