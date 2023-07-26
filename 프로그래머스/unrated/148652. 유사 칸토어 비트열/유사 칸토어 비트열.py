def back(n, x):
    if n == 1:
        return '11011'
    parent = back(n-1, x // 5)
    x = parent[x % 5]
    if x == '1':
        return '11011'
    else:
        return '00000'
    

def solution(n, l, r):
    ans = []
    start = (l - 1) // 5
    if not r % 5:
        end = r // 5
    else: end = (r // 5) + 1
    
    for i in range(start, end):
        ans.append(back(n, i))
        
    l = (l - 1) % 5
    r = -(5 - (r % 5))
    if r == -5:
        return ''.join(ans)[l:].count('1')
    return ''.join(ans)[l:r].count('1')