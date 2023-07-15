def solution(n, left, right):
    s_row, s_col = divmod(left, n)
    e_row, e_col = divmod(right, n)
    
    arr = []
    
    for i in range(s_row+1, n+1):
        if i > e_row + 1: break
        for j in range(i, n+1):
            if j == i:
                for k in range(i):
                    if k == 0: continue 
                    arr.append(j)
            arr.append(j)
    e_col = (len(arr) - n) + e_col
    return arr[s_col:e_col+1]
            