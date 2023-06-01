from collections import deque

def solution(A, B):
    if A == B:
        return 0
    
    A = deque(A)
    
    for i in range(1, len(A)+1):
        A.rotate(1)
        if list(A) == list(B):
            return i
    
    return -1