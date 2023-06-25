def solution(X, Y):
    x_cnt = [0] * 10
    y_cnt = [0] * 10
    
    for i in X:
        x_cnt[int(i)] += 1
    for i in Y:
        y_cnt[int(i)] += 1
        
    result = []
    
    for index, n in enumerate(zip(x_cnt, y_cnt)):
        if n[0] > 0 and n[1] > 0:
            s_cnt = min(n[0], n[1]) * 2
            for _ in range(s_cnt // 2):
                result.append(index)

    if not result: return '-1'
    elif not sum(result): return '0'
    else:
        result.sort(reverse=True)
        return ''.join(map(str, result))
        
            