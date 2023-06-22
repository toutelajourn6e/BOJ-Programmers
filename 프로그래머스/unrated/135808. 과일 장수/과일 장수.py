def solution(k, m, score):
    n = len(score)
    score.sort(reverse=True)
    score = score[:(n//m)*m]
    result = [score[i:i+m] for i in range(0, n, m)]
    sum_v = 0
    
    for i in result:
        if len(i) > 0:
            sum_v += min(i) * m
            
    return sum_v
    