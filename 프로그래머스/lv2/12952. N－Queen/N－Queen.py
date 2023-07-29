def is_promissing(col, i, dia, depth):
    if col & 1 << i: return False
    if dia[depth] & 1 << i: return False
    return True
    

def solution(n):
    ans = 0
    dia = [0 for _ in range(n)]
    
    def n_queen(col, depth):
        nonlocal ans
        if depth == n:
            ans += 1
            return
        
        for i in range(n):
            if is_promissing(col, i, dia, depth):
                for idx, j in enumerate(range(depth+1, n)):
                    if i - (idx+1) >= 0:
                        dia[j] |= 1 << (i-(idx+1))
                    dia[j] |= 1 << (i+(idx+1)) 
                n_queen(col | 1 << i, depth+1)
                for idx, j in enumerate(range(depth+1, n)):
                    if i - (idx+1) >= 0:
                        dia[j] = dia[j] & ~(1 << (i-(idx+1)))
                    dia[j] = dia[j] & ~(1 << (i+(idx+1)))
                      
    n_queen(0, 0)
    return ans