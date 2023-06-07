def solution(dots):
    dots.sort(key = lambda x: x[0])
    n = len(dots)
    m = []
    m.append((dots[1][1] - dots[0][1]) / (dots[1][0] - dots[0][0]))
    m.append((dots[3][1] - dots[2][1]) / (dots[3][0] - dots[2][0]))
    m.append((dots[2][1] - dots[0][1]) / (dots[2][0] - dots[0][0]))
    m.append((dots[3][1] - dots[1][1]) / (dots[3][0] - dots[1][0]))
    m.append((dots[3][1] - dots[0][1]) / (dots[3][0] - dots[0][0]))
    m.append((dots[2][1] - dots[1][1]) / (dots[2][0] - dots[1][0]))
    
    if m[0] == m[1] or m[2] == m[3] or m[4] == m[5]:
        return 1
    return 0
    