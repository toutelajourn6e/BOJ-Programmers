def solution(a, b, n):
    ans = 0
    empty = n
    cola = 0
    
    while empty // a > 0:
        change = empty // a
        empty %= a
        cola += b * change
        ans += cola
        empty += cola
        cola = 0
        
    return ans