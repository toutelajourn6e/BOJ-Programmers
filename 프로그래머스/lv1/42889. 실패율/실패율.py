from collections import Counter, deque

def solution(N, stages):
    n = len(stages)
    stages = Counter(stages)
    result = []
    
    for stage in range(1, N+1):
        if n == 0:
            result.append((stage, stages[stage]))
            continue
        result.append((stage, stages[stage]/n))
        n -= stages[stage]
        
    result.sort(key=lambda x: (x[1], -x[0]), reverse=True)
    result = [i for i, j in result]
    
    return result