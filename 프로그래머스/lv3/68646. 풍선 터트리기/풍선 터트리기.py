def solution(a):
    INF = 1_000_000_001
    check = [0] * len(a)
    left, right = INF, INF
    
    for i in range(len(a)):
        if a[i] < left:
            left = a[i]
            check[i] = 1
        
    for i in range(len(a)-1, -1, -1):
        if a[i] < right:
            right = a[i]
            check[i] = 1
            
    return sum(check)