def solution(s):
    p = 0
    y = 0
    
    p += s.count('p')
    p += s.count('P')
    y += s.count('y')
    y += s.count('Y')
    
    if p == y:
        return True
    else:
        return False