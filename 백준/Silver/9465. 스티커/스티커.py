
t = int(input())

for _ in range(t):
    n = int(input())
    d = [[0,0,0] for _ in range(n+1)]
    one = [0] + list(map(int, input().split()))
    two = [0] + list(map(int, input().split()))
    
    for n in range(1, n+1):
        d[n][0] = max(d[n-1][0], d[n-1][1], d[n-1][2])
        d[n][1] = max(d[n-1][0], d[n-1][2]) + one[n]
        d[n][2] = max(d[n-1][0], d[n-1][1]) + two[n]
        
    print(max(d[n]))
    