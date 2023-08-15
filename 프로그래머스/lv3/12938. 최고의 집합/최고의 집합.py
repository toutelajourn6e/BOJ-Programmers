def solution(n, s):
    quotient, remainder = divmod(s, n)
    if not quotient: return [-1]
    
    ans = [quotient] * n
    idx = len(ans) - 1
    while remainder:
        ans[idx] += 1
        remainder -= 1
        idx = (idx - 1) % len(ans)
    
    return ans