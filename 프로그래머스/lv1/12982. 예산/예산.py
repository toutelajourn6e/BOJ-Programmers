def solution(d, budget):
    d = sorted(d)
    for i in range(len(d)):
        budget -= d[i]
        if budget < 0:
            return i
    else:
        return len(d)
            