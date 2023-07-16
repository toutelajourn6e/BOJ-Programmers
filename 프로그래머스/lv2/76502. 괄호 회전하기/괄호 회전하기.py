from collections import deque

def check(s):
    A, B, C = '()', '{}', '[]'
    while True:
        before = len(s)
        s = s.replace(A, '').replace(B, '').replace(C, '')
        after = len(s)
        if before == after: break
    return 1 if not s else 0
        
    

def solution(s):
    s = deque(list(s))
    result = 0
    
    for _ in range(len(s)):
        s.rotate(-1)
        result += check(''.join(list(s)))
        
    return result
    