case = 1
ans = 0

while True:
    l, p, v = map(int, input().split())
    if l == 0 and p == 0 and v == 0:
        break
    ans += (v // p) * l
    
    if v % p < l:
        ans += (v % p)
    else:
        ans += l
    
    print(f'Case {case}: {ans}')
    ans = 0
    case += 1