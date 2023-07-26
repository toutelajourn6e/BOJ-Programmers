from functools import reduce

def solution(data, col, row_begin, row_end):
    data = sorted(data, key=lambda x: (x[col-1], -x[0]))
    ans = []
    
    for i in range(row_begin, row_end+1):
        S_i = 0
        for j in data[i-1]:
            S_i += j % i
        ans.append(S_i)
        
    ans = reduce(lambda x, y: x ^ y, ans)
    return ans