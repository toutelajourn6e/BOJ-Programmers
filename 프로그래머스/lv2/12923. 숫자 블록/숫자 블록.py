def cal(num):
    if num == 1: return 0
    elif num == 2: return 1
    n = 10000000
    if num // 2 < 10000000: n = num // 2
    for i in range(n, 1, -1):
        if not num % i:
            return i
    return 1

def solution(begin, end):
    ans = [0] * ((end - begin)+1)
    
    for i in range(len(ans)):
        ans[i] = cal(begin + i)
    
    return ans
        