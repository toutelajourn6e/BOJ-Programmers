from math import factorial as f

def solution(n, k):
    result = []
    digit = [i for i in range(1, n+1)]
    k -= 1
    
    while digit:
        idx, k = divmod(k, f(len(digit)-1))
        result.append(digit.pop(idx))
        
    return result