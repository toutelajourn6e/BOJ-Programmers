import sys
input = sys.stdin.readline

n, m = map(int, input().split())

chk = [False] * (n+1)
rs = []

def back():
    if len(rs) == m:
        print(' '.join(map(str, rs)))
        return
    
    for i in range(1, n+1):
        if not chk[i]:
            chk[i] = True
            rs.append(i)
            back()
            chk[i] = False
            rs.pop()
            
back()