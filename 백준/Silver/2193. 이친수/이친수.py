n = int(input())
d = [[0]*2 for i in range(n+1)]

for i in range(1, n+1):
    for j in range(2):
        if i == 1 and j == 1:
            d[i][j] += 1
            
        if j == 0:
            d[i][j] += d[i-1][1]

        d[i][j] += d[i-1][0]
        
print(sum(d[n]))